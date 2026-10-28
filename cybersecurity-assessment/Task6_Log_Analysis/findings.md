# Task 6: Decode and Interpret Security Logs

## Objective
Analyze synthetic authentication logs to identify unusual login patterns.

## Dataset
The dataset contains 10 synthetic authentication events.

## Results
- Successful login events: 4
- Failed login events: 6
- IP 203.0.113.25: 4 failed login events
- IP 198.51.100.14: 2 failed login events

## Findings
The repeated failed login events associated with 203.0.113.25 warrant further investigation.

The events alone do not establish whether the activity was malicious or whether any account was compromised.

## Recommendations
1. Review authentication logs for additional context.
2. Apply multi-factor authentication.
3. Use appropriate rate limiting and account-protection controls.
4. Monitor repeated authentication failures.
5. Investigate suspicious events before drawing conclusions.

## Limitations
This is a synthetic dataset created for educational purposes. It does not represent a real security incident.
