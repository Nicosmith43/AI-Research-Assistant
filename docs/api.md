# API Design

## Authentication

POST /auth/register

Create a new user account.

POST /auth/login

Authenticate a user and return a JWT.

GET /auth/me

Return the currently logged in user.

---

## Papers

GET /papers/search

Search academic papers.

GET /papers/{paper_id}

Retrieve information about a paper.

POST /papers/save

Save a paper to the user's library.

GET /papers/saved

Return saved papers.

DELETE /papers/{paper_id}

Remove a saved paper.

---

## GitHub

GET /github/search

Search GitHub repositories.

GET /github/repository/{owner}/{repo}

Retrieve repository information.

---

## AI

POST /ai/chat

Ask research questions.

POST /ai/summarize

Generate a paper summary.

POST /ai/compare

Compare two papers.

POST /ai/explain

Explain a difficult concept.

POST /ai/quiz

Generate quiz questions.

POST /ai/roadmap

Generate a learning roadmap.

---

## Collections

POST /collections

Create a collection.

GET /collections

Retrieve all collections.

PUT /collections/{id}

Update a collection.

DELETE /collections/{id}

Delete a collection.

---

## Notes

POST /notes

Create notes.

GET /notes

Retrieve notes.

PUT /notes/{id}

Update notes.

DELETE /notes/{id}

Delete notes.

---

## Conversations

GET /chat/history

Retrieve previous conversations.

DELETE /chat/history/{id}

Delete a conversation.