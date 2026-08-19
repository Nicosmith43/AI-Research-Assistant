# Architecture

The AI Research Assistant follows a modern client-server architecture.

The React frontend is responsible for displaying the user interface and handling user interactions. All requests are sent to the FastAPI backend through REST APIs.

The FastAPI backend handles:

- Authentication
- Business logic
- Database operations
- AI requests
- External API integrations

MongoDB stores all user data including accounts, saved papers, conversations, collections, and notes.

The backend communicates with external services such as OpenAI, arXiv, Semantic Scholar, GitHub, Wikipedia, and CrossRef to retrieve research information and generate AI-powered responses.

## High-Level Architecture

```text
                    User
                      │
                      ▼
             React + TypeScript
                      │
                 REST API Calls
                      │
                      ▼
                 FastAPI Backend
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
   MongoDB         OpenAI API     External APIs
                                     │
             ┌────────────┬──────────┴──────────┐
             ▼            ▼          ▼          ▼
          arXiv      Semantic    GitHub    Wikipedia
                        Scholar              CrossRef
```

## Responsibilities

### Frontend

- Login
- Dashboard
- Search Interface
- Chat Interface
- Collections
- Notes
- User Settings

### Backend

- Authentication
- Search APIs
- AI Processing
- Data Validation
- Database Management
- External API Integration

### Database

Stores:

- Users
- Saved Papers
- Collections
- Notes
- Chat History