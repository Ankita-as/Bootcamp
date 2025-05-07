```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database

    User->>Frontend: Login form
    Frontend->>Backend: API Request
    Backend->>Database: Verify credentials
    Database-->>Backend: Result
    Backend-->>Frontend: Success/Failure
    Frontend-->>User: Show message
```
