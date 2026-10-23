# Runbook: Azure Payment-Service High Latency & OOM Incident Response

## Service Overview
- **Service Name**: `payment-service`
- **Azure Resource Group**: `rg-prod-eastus-payments`
- **Cluster**: Azure Kubernetes Service (`aks-prod-eastus-01`)
- **Current Version**: `v2.1.0-rc2` (Deployed 2026-10-22)
- **Stable Rollback Target**: `v2.0.4`
- **SLO Target**: 99.95% availability, p99 latency < 250ms.

## Incident Signatures & Diagnostics
### Signature A: Memory Leak & Latency Cascade
- **Symptoms**: Gradual heap growth in Node/Go worker pods, p99 latency spiking above 1800ms, HTTP 504 Gateway Timeouts from Azure Application Gateway.
- **Root Cause**: Unbounded redis connection pooling and cache eviction failure introduced in `v2.1.0-rc2` commit `8a4f91c`.
- **Diagnostic Step**: Execute `check_service_health` with parameter `{"service": "payment-service"}` to verify pod heap allocations and active connection pool size.

## Mitigation & Recovery Procedures
1. **Immediate Rollback**:
   - Revert pod deployment to stable tag `v2.0.4`.
   - High-Stakes Action: Requires explicit incident commander voice confirmation ("Are you sure you want to rollback payment-service from v2.1.0 to v2.0.4?").
   - Command: `trigger_service_rollback(service="payment-service", targetVersion="v2.0.4")`.
2. **Post-Rollback Verification**:
   - Query Azure telemetry to ensure latency drops below 200ms and HTTP 500 error rate reaches 0.00%.
3. **Post-Mortem & Ticket Filing**:
   - File incident report in Jira/ServiceNow using `file_incident_postmortem`.

## Escalation Policy
- Severity 1 (S1): PagerDuty page to On-Call SRE Lead within 5 minutes.
- Stakeholder updates every 15 minutes in Slack channel `#warroom-azure-payments`.
