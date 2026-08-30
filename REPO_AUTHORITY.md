# Repository Authority

Canonical service hostname: `blac.codestra.media`
Canonical DNS A target: `37.27.128.39`
DNS TTL: `600`

This repository is the principal source authority for the Codestra Blackbox Exporter deployment/configuration. Do not introduce alternate public hostnames or legacy domain names in configuration, documentation, examples, probes, or deployment manifests.

Exposure policy: PRIVATE. DNS may resolve publicly, but the Blackbox Exporter administration/metrics endpoint must be reachable only from approved monitoring/private networks. Probe targets may be public or private according to an approved probe policy.

Upstream/downstream: Prometheus (`prom.codestra.media`) calls Blackbox Exporter for synthetic probes -> Blackbox Exporter probes approved HTTP/TCP/TLS endpoints -> Prometheus stores results -> Grafana (`graf.codestra.media`) visualizes them -> Alertmanager (`aler.codestra.media`) routes synthetic-failure alerts.

Persistent branch model: `main`, `development`, `test`, `staging`, `production`. Temporary branches: `feature/*`, `fix/*`, `upgrade/*`, `security/*`, `docs/*`, `hotfix/*`, `release/*`, `rollback/*`.

Promotion: feature/fix/upgrade/security -> development -> test -> staging -> production -> main. Never upgrade directly on staging, production, or main.
