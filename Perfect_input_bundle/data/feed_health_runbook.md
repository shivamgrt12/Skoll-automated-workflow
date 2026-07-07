# Surveillance Feed Health - Runbook

A collection day is clean only when the dashboard is green AND there is no open
on-call alert AND no unresolved ingestion error for that day. A green dashboard
alone is not sufficient. Degraded days are reported with the alert id and the
error id behind the call. Incomplete days are footnoted in the audit.
