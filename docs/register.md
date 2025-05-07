```markdown
# Registration Flow

This section describes the flow of the registration process.

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Database

    User->>Frontend: Fill registration form
    Frontend->>Backend: Send registration data
    Backend->>Database: Save user data
    Database-->>Backend: Success
    Backend-->>Frontend: Registration successful
    Frontend-->>User: Show success message