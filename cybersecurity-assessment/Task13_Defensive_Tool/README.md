# Task 13: Defensive Security Log Analyzer

## Objective
Build a small defensive security tool that analyzes authentication logs and identifies repeated failed login attempts.

## Technologies
- Python 3
- Linux / Ubuntu WSL

## Features
- Counts successful login events.
- Counts failed login events.
- Identifies IP addresses with repeated failures.
- Reports malformed or unrecognized entries.
- Handles missing input files.

## How to Run

```bash
python3 log_analyzer.py ../Task6_Log_Analysis/sample_auth.log

## Step 2: Save the Task 6 investigation report

Run:

```bash
cat > ~/cybersecurity-assessment/Task6_Log_Analysis/investigation_report.md << 'EOF'
# Task 6: Decode and Interpret Security Logs

## 1. Objective
Analyze synthetic authentication logs to identify unusual patterns and recommend defensive measures.

## 2. Dataset
The dataset contains 10 synthetic authentication events.

## 3. Results
| Observation | Result |
|---|---:|
| Successful login events | 4 |
| Failed login events | 6 |
| Failed events from 203.0.113.25 | 4 |
| Failed events from 198.51.100.14 | 2 |

## 4. Analysis
The repeated failed login events associated with 203.0.113.25 warrant further investigation.

The available events do not establish whether the activity was malicious or whether an account was compromised.

## 5. Recommendations
1. Review additional authentication and system logs.
2. Enable multi-factor authentication.
3. Apply appropriate rate limiting and account-protection controls.
4. Monitor repeated authentication failures.
5. Investigate suspicious activity before drawing conclusions.

## 6. Limitations
The dataset is synthetic and does not represent a real incident. IP addresses and event counts alone cannot establish an attacker's identity or intent.

## 7. Conclusion
The analysis identified repeated failed login activity suitable for further investigation. Additional evidence would be required to determine the cause.
