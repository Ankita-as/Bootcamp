# Registration Flow

This page explains the registration process for new users.

```mermaid
sequenceDiagram
  participant User
  participant App
  participant DB

  User->>App: Submit registration form
  App->>DB: Save user data
  DB-->>App: Success response
  App-->>User: Registration complete