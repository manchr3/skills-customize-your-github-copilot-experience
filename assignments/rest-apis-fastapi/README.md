# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build REST APIs using the FastAPI framework, practicing API design, routing, request handling, and response formatting.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description

Install FastAPI and create a basic application structure with a root endpoint.

#### Requirements

Completed program should:

- Install FastAPI and Uvicorn dependencies
- Create a FastAPI app instance
- Add a GET endpoint at "/" that returns a welcome message
- Run the server and verify it responds

### 🛠️ Implement CRUD Endpoints

#### Description

Add endpoints for creating, reading, updating, and deleting items in a simple in-memory data store.

#### Requirements

Completed program should:

- Add a GET /items endpoint to retrieve all items
- Add a POST /items endpoint to create a new item
- Add a GET /items/{item_id} endpoint to retrieve a specific item
- Add a PUT /items/{item_id} endpoint to update an item
- Add a DELETE /items/{item_id} endpoint to delete an item
- Use Pydantic models for request/response validation