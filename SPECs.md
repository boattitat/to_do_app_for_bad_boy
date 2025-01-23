```mermaid
sequenceDiagram
    participant Client
    participant A as session manager
    participant B as duplicator
    participant C as finalizer
    participant DB as Database

    Client->>A: POST /submit TODO
    A->>A: Validate & transform TODO
    A->>B: POST /processStep
    B->>B: duplicate every record
    B-->>A: 200 OK (with data)
    A->>C: POST /finalize
    C->>C: Final processing
    C-->>A: 200 OK (with data) 
    A->>DB: Insert records into DB
    DB-->>A: Insert successful
    A-->>Client: 201 Created (final response)

    Client->>A: GET
    A->>DB: Get records from DB
    DB-->>A: GET successful
    A-->>Client: 200 OK (with records)
```
