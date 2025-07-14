# Hack the system
Simple system, takes in user document (CV), job description, and runs it against an elaborate set of rules to determine how likely it is to beat an ATS.

1. Out of the gate we need a deterministic scoring system
2. Strong ATS signals (perhaps subscribe to the best ones?)

### We return a score saying
likelihood of passing an ATS for the role:
0-100

Interestingness relative to job
A-F and S tiers

We also return recommendations based on areas of weakness.
