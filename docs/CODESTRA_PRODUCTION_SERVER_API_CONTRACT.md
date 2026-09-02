# Codestra Blackbox Exporter Production Server and Native API Contract

## Authority

- Repository: `appolon1908-hue/Codestra-Blackbox-Exporter`
- Role: controlled synthetic HTTPS, TLS, DNS, TCP, ICMP, and approved gRPC evidence authority
- Canonical hostname: `blac.codestra.media`
- Central production host: `37.27.128.39`
- Status: `SOURCE_CONTRACT_PREPARED_NOT_DEPLOYED`

Blackbox Exporter owns probe modules, target allowlists, SSRF controls, release evidence, and rollback. It does not own arbitrary Internet scanning, business actions, credentials, or application mutation.

## Native API surface

| Method | Path | Purpose | Boundary |
|---|---|---|---|
| `GET` | `/-/healthy` | exporter health | private/read-only |
| `GET` | `/metrics` | exporter self-metrics | private Prometheus scrape |
| `GET` | `/probe` | controlled synthetic probe | authenticated/internal module and destination allowlists |

Unexpected `404`, unhandled `5xx`, arbitrary target selection, credential-bearing URLs, or a public unrestricted `/probe` endpoint blocks production.

## Probe security policy

- Permit only source-controlled module and destination allowlists.
- Resolve and validate every target before and after DNS resolution.
- Deny loopback, link-local, metadata, multicast, unspecified, private, reserved, and disallowed internal addresses unless the exact internal destination is explicitly reviewed for the private monitoring plane.
- Protect against DNS rebinding and redirect-to-disallowed-address behavior.
- Limit methods, redirects, TLS versions, response sizes, timeouts, concurrency, and egress.
- Never accept embedded credentials, tokens, cookies, secret query strings, or arbitrary operator-supplied targets.
- Native metrics and probe endpoints remain private.

## Production gates

```text
PROTECTED_PRODUCTION_SHA=PASS
MODULE_ALLOWLIST=PASS
DESTINATION_ALLOWLIST=PASS
SSRF_TESTS=PASS
METADATA_ADDRESS_DENIAL=PASS
DNS_REBINDING_DENIAL=PASS
REDIRECT_POLICY=PASS
EGRESS_POLICY=PASS
TIMEOUT_LIMITS=PASS
RESPONSE_SIZE_LIMITS=PASS
CONCURRENCY_LIMITS=PASS
IMMUTABLE_IMAGE_DIGEST=PASS
IMAGE_SIGNATURE=PASS
SBOM=PASS
PROVENANCE=PASS
SECRET_SCAN=PASS
ROLLBACK_MANIFEST=PASS
```

## Runtime certification

```text
GET_/-/healthy=PASS
GET_/metrics=PASS
GET_/probe_ALLOWLISTED_TARGET=PASS
GET_/probe_UNAPPROVED_TARGET=DENIED
LOOPBACK_DENIED=PASS
LINK_LOCAL_DENIED=PASS
METADATA_DENIED=PASS
DNS_REBINDING_DENIED=PASS
CREDENTIAL_TARGET_DENIED=PASS
TIMEOUT_CONTROL=PASS
RESPONSE_SIZE_CONTROL=PASS
CONCURRENCY_CONTROL=PASS
UNEXPECTED_404=0
UNEXPECTED_5XX=0
SOURCE_RUNTIME_DRIFT=0
```

Use only approved non-transactional endpoints. Do not probe actions that create leads, messages, payments, calls, orders, certificates, or provider effects.

## Repository-first remediation

Preserve the old healthy exporter when a probe or security test fails. Fix modules, allowlists, validation, or runtime configuration here with regression tests; commit/push; obtain exact-head CI/review; merge normally; rebuild/sign; update the BOM; and retry. Never add a target only on the server.

## Safety

This document does not deploy Blackbox Exporter or activate targets. SSH changes, business writes, communications delivery, provider actions, lending, payments, and trading remain outside scope and disabled.