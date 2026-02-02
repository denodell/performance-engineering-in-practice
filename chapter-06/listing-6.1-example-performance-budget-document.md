# Performance Budget
Last updated: 2026-02-15

## Goals
These budgets support our user-centered performance goals:
- Checkout API response time under 200ms at p95
- Mobile cold start under 2s on devices with 4GB RAM
- LCP under 2.5s for 75% of mobile web users

## Current Status
| Resource  | Threshold | Current | Headroom | Owner | Last Measured |
|-----------|-----------|---------|----------|-------|---------------|
| /api/checkout p95 | 200ms | 168ms | 32ms | Payments | 2026-02-04 |
| /api/search p95 | 150ms | 142ms | 8ms | Search | 2026-02-04 |
| iOS cold start (iPhone 14) | 2.0s | 1.6s | 0.4s | Mobile | 2026-01-28 |
| Android cold start (Pixel 7) | 2.5s | 2.2s | 0.3s | Mobile | 2026-01-28 |
| Android APK size | 50MB | 43MB | 7MB | Mobile | 2026-01-28 |
| Main JS bundle (gzip) | 200KB | 172KB | 28KB | Frontend | 2026-02-04 |

## Exception Process
| Exception Size | Approver | Turnaround | Documentation |
|----------------|----------|------------|---------------|
| < 10%, offset this sprint | Technical owner | Immediate | PR comment |
| 10-25% or not offset | Engineering manager | 1-2 days | Decision log entry |
| > 25% or permanent | Senior leadership | Up to 1 week | Business justification |

## Decision Log
| Date | Budget | Change | Reason | Approver | Conditions |
|------|--------|--------|--------|----------|------------|
| 2026-02-15 | /api/checkout p95 | 200ms → 250ms | Added fraud detection | M. Chen | Review after 90 days |
| 2025-11-15 | Main JS bundle | 230KB → 210KB | Tree-shook icons | - | Condition met |
| 2025-06-15 | Main JS bundle | 200KB → 230KB | Added 360° viewer | J. Smith | Reduce to 210KB by Q3 |
