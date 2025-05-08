# Login Flow

This page explains the login workflow used in our system.

```mermaid
flowchart TD
  A[User enters login info] --> B{Is Info Valid?}
  B -- Yes --> C[Redirect to Dashboard]
  B -- No --> D[Show Error Message]