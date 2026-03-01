# Architecture

This document describes the high-level architecture of **KriptoStack** (backend), focusing on the database design and API boundaries.

## Database (ERD)
- Source: `docs/erd.dbml`
- Diagram: `docs/erd.png`

### Core relationships
- **User (1) → (0..N) Wallet**

### Key tables (conceptual)

- `wallets`: user portfolios/accounts by provider (Revolut, Kraken, etc.)