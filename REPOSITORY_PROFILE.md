# Repository Profile — `Codestra-Blackbox-Exporter`

## Identity

- **Repository:** `appolon1908-hue/Codestra-Blackbox-Exporter`
- **Category:** Observability exporter — synthetic probes
- **Visibility:** `public`
- **Default branch:** `main`
- **Canonical hostname:** `blac.codestra.media`
- **Exposure:** Internal/private only; the exporter is not a public proxy
- **Authority:** Primary governed HTTP, TCP, DNS, TLS, and ICMP availability/latency probe authority

## Purpose

Executes side-effect-free synthetic probes for customer paths and infrastructure dependencies while preserving target ownership and policy in Prometheus/infrastructure configuration.

## Owns

- Blackbox Exporter runtime and approved probe modules
- TLS verification, timeout, redirect, IP-family, capability, and private-network policy
- Probe validation, immutable packaging, upgrade, and rollback source

## Does not own

- Arbitrary user-supplied targets or an open proxy
- Business transactions, calls, messages, trades, form submissions, or provider effects
- Prometheus target inventory as an independent source of truth

## Key integrations

- Prometheus target and relabel configuration
- Grafana and Alertmanager
- Public and private DNS/HTTPS/TCP dependencies approved by infrastructure policy

## Current priorities

1. Keep probe modules bounded, side-effect-free, and target-allowlisted
2. Validate certificate expiry, DNS, content, latency, TCP, and dependency-health probes
3. Prove no unsafe redirects, IP-family fallback, arbitrary targets, or mutation paths
4. Add immutable packaging, upgrade, rollback, and target-owner evidence

## Governance and safety

- Promotion model: `feature/docs/fix/security/upgrade -> development -> test -> staging -> production -> main`.
- Native port `9115` must remain private; `blac.codestra.media` must not expose the exporter as a public probe service.
- Never commit credentials, private keys, customer payloads, secret URLs, or sensitive probe evidence.
- Every target requires ownership, purpose, sensitivity, frequency, and side-effect review.
- Merge does not activate probes, alter Prometheus targets, send traffic, expose ports, or deploy software.

## Account-wide catalog

See `appolon1908-hue/documentaions/REPOSITORY_CATALOG.md`.
