# Codestra Blackbox Exporter

This repository is the service authority for active HTTP, HTTPS, TCP, DNS, and ICMP probes. `appolon1908-hue/Codestra-Prometheus` owns the approved target list, target labels, recording rules, alerts, and retention.

## Security boundary

Blackbox Exporter can initiate network connections to a caller-selected target, so `/probe` is a sensitive internal control surface. It runs only on the external private Docker network `codestra-observability`, has no host port, no public DNS record, and no Caddy/Kong route. Only the authoritative Prometheus service and approved observability operators may reach `blackbox-exporter:9115`.

The container runs as UID/GID 65534 with a read-only filesystem, drops every capability, and adds back only `NET_RAW` for ICMP. HTTPS probes require TLS and verify certificates. IPv4 fallback is disabled so probe results do not silently change address families.

## Module policy

Approved modules are:

- `https_2xx`: public HTTPS health with certificate verification and redirects;
- `http_2xx_internal`: private HTTP health with only 200/204 and no redirects;
- `tcp_connect`: bounded TCP reachability;
- `dns_codestra_a`: `codestra.co` A-record resolution through an approved DNS target;
- `icmp_private`: private-host ICMP reachability.

New modules require a PR, explicit timeout, threat review, and staging evidence. Do not add credentials, arbitrary headers, insecure TLS, unrestricted redirects for internal probes, or target addresses to this repository. Targets belong to Prometheus file discovery and carry `environment`, `server`, `application`, `service`, `tenant_scope=aggregate`, and `probe_enabled` labels.

## Validation

```bash
cp .env.example .env
# Set the reviewed image digest.
docker compose -f deploy/compose.yaml config
docker compose -f deploy/compose.yaml up -d
# From Prometheus/private observability network only:
curl --fail 'http://blackbox-exporter:9115/probe?module=https_2xx&target=https://codestra.co/'
```

Before activation, prove the endpoint is unreachable publicly, every target is approved, `probe_success` works for positive and negative tests, TLS expiry is reported, ICMP capability is limited, required labels are present, and rollback succeeds. Deployment is a separate approved operation.

Promotion is `feature/* -> development -> test -> staging -> production -> main`. Merging does not deploy.
