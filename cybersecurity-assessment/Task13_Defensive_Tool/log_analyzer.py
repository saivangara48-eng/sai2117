#!/usr/bin/env python3

from collections import Counter
from pathlib import Path
import re
import sys

FAILURE_THRESHOLD = 3

def analyze_logs(log_file):
    path = Path(log_file)

    if not path.is_file():
        print(f"Error: File not found: {path}")
        return 1

    successful = 0
    failed = 0
    failed_ips = Counter()
    malformed = 0

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if "LOGIN_SUCCESS" in line:
                successful += 1

            elif "LOGIN_FAILURE" in line:
                failed += 1

                match = re.search(r"\bip=(\S+)", line)

                if match:
                    failed_ips[match.group(1)] += 1
                else:
                    malformed += 1

            else:
                malformed += 1

    print("\n=== SECURITY LOG ANALYSIS REPORT ===")
    print(f"Successful logins: {successful}")
    print(f"Failed logins: {failed}")
    print(f"Unrecognized or malformed entries: {malformed}")

    print("\n=== REPEATED FAILED LOGIN ACTIVITY ===")

    alerts = 0

    for ip, count in sorted(failed_ips.items()):
        if count >= FAILURE_THRESHOLD:
            print(f"REVIEW REQUIRED: {ip} had {count} failed login attempts")
            alerts += 1

    if alerts == 0:
        print("No IP addresses met the alert threshold.")

    print("\nNote: Repeated failures warrant investigation but do not prove an attack.")

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 log_analyzer.py <log_file>")
        sys.exit(2)

    sys.exit(analyze_logs(sys.argv[1]))

