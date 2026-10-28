# Test Cases: Defensive Security Log Analyzcer

## Test 1: Normal analysis
Input: Synthetic authentication log containing 10 events.
Expected: 4 successful logins and 6 failed logins.
Result: PASS — output matched the expected counts.

## Test 2: Repeated failed logins
Input: Log containing 4 failed login events from 203.0.113.25.
Expected: An alert requiring investigation.
Result: PASS — the tool reported 4 failed attempts.

## Test 3: Missing file
Input: A nonexistent log file.
Expected: An error message indicating that the file was not found.
Result: PASS - the tool displayed a file-not-found error.
## Limitations
Repeated failures are suspicious indicators, not proof of malicious activity.
