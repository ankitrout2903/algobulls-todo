# Algobulls Todo API

## Table of Contents
- [Algobulls Todo API](#algobulls-todo-api)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
      - [Or you can run it locally](#or-you-can-run-it-locally)
  - [API Endpoints](#api-endpoints)
    - [Get a list of all the tasks](#get-a-list-of-all-the-tasks)
    - [Create a new task](#create-a-new-task)
    - [Get a task by id](#get-a-task-by-id)
    - [Update a task by id](#update-a-task-by-id)
    - [Delete a task by id](#delete-a-task-by-id)
  - [Authentication](#authentication)
    - [Register a new user](#register-a-new-user)
## Getting Started
The API is available at [https://algobulls-todo.onrender.com/](https://algobulls-todo.onrender.com/)

You can see the documentation at [https://algobulls-todo.onrender.com/](https://algobulls-todo.onrender.com/)

#### Or you can run it locally
1. Clone the repository
2. Install the dependencies
```bash
pip install -r requirements.txt
```
3. Run the server
```bash
python manage.py runserver
```
4. The API is now available at [http://localhost:8000/](http://localhost:8000/)
5. You can see the documentation at [http://localhost:8000/](http://localhost:8000/api/schema/swagger-ui/)
6. You can also see the documentation at [http://localhost:8000/](http://localhost:8000/api/schema/redoc/)

## API Endpoints

### Get a list of all the tasks
`GET /api/tasks/`
```bash
curl -X GET https://algobulls-todo.onrender.com/api/todos/ -u "username:password"
```

### Create a new task
`POST /api/tasks/`
```bash
curl -X POST https://algobulls-todo.onrender.com/api/todos/ -u "username:password" -H "Content-Type: application/json" -d '{"title": "string", "description": "string", "status": "string", "due_date": "string", "tags": ["string"]}'
```

### Get a task by id
`GET /api/tasks/{id}/`
```bash
curl -X GET https://algobulls-todo.onrender.com/api/todos/{id}/ -u "username:password"
```

### Update a task by id
`PUT /api/tasks/{id}/`
```bash
curl -X PUT https://algobulls-todo.onrender.com/api/todos/{id}/ -u "username:password" -H "Content-Type: application/json" -d '{"title": "string", "description": "string", "status": "string", "due_date": "string", "tags": ["string"]}'
```

### Delete a task by id
`DELETE /api/tasks/{id}/`
```bash
curl -X DELETE https://algobulls-todo.onrender.com/api/todos/{id}/ -u "username:password"
```

## Authentication

### Register a new user
`POST /api/auth/register/`
```bash
curl -X POST https://algobulls-todo.onrender.com/api/auth/register/ -H "Content-Type: application/json" -d '{"username": "string", "password": "string"}'
```


## Table of Contents

1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
    - [1. Register User](#register-user)
    - [2. Get Todos](#get-todos)
    - [3. Create Todo](#create-todo)
    - [4. Get Todo by ID](#get-todo-by-id)
    - [5. Update Todo](#update-todo)
    - [6. Partially Update Todo](#partially-update-todo)
    - [7. Delete Todo](#delete-todo)

## 1. Introduction

This document provides detailed information about the RESTful API for the application available at [https://ankitrout2903.pythonanywhere.com/](https://ankitrout2903.pythonanywhere.com/).

## 2. Authentication

The API uses token-based authentication. To access secured endpoints, include the authentication token in the headers of your requests.

## 3. Endpoints

### 1. Register User

#### Endpoint

- **Method**: POST
- **Path**: `/api/auth/register/`

#### Request

- **Parameters**: None

#### Request Body

```json
{
  "username": "7mFeEYYHxY9u8.n",
  "password": "string"
}
```

#### Response

- **Status Code**: 201 Created
- **Body**: 

```json
{
  "id": 0,
  "username": "pQ6RIvu03pC6Zsx+Ws6ef87LvxwjEo0CmqCfeCqzehfhEtpHAk0AY.6AFsThgy9I5kFQkFNb4WhH6U0-qSxNZEGoA"
}
```

### 2. Get Todos

#### Endpoint

- **Method**: GET
- **Path**: `/api/todos/`

#### Request

- **Parameters**: None

#### Response

- **Status Code**: 200 OK
- **Body**: 

```json
[
  {
    "id": 0,
    "title": "string",
    "description": "string",
    "status": "OPEN",
    "due_date": "2023-12-08T15:59:52.481Z",
    "timestamp": "2023-12-08T15:59:52.481Z",
    "tags": [
      "string"
    ]
  }
]
```

### 3. Create Todo

#### Endpoint

- **Method**: POST
- **Path**: `/api/todos/`

#### Request

- **Parameters**: None

#### Request Body

```json
{
  "title": "string",
  "description": "string",
  "status": "OPEN",
  "due_date": "2023-12-08T15:59:52.482Z",
  "tags": [
    "string"
  ]
}
```

#### Response

- **Status Code**: 201 Created
- **Body**: 

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "status": "OPEN",
  "due_date": "2023-12-08T15:59:52.483Z",
  "timestamp": "2023-12-08T15:59:52.483Z",
  "tags": [
    "string"
  ]
}
```

### 4. Get Todo by ID

#### Endpoint

- **Method**: GET
- **Path**: `/api/todos/{id}/`

#### Request

- **Parameters**:
  - `id` (integer) - A unique integer value identifying this todo.

#### Response

- **Status Code**: 200 OK
- **Body**: 

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "status": "OPEN",
  "due_date": "2023-12-08T15:59:52.484Z",
  "timestamp": "2023-12-08T15:59:52.484Z",
  "tags": [
    "string"
  ]
}
```

### 5. Update Todo

#### Endpoint

- **Method**: PUT
- **Path**: `/api/todos/{id}/`

#### Request

- **Parameters**:
  - `id` (integer) - A unique integer value identifying this todo.

#### Request Body

```json
{
  "title": "string",
  "description": "string",
  "status": "OPEN",
  "due_date": "2023-12-08T15:59:52.486Z",
  "tags": [
    "string"
  ]
}
```

#### Response

- **Status Code**: 200 OK
- **Body**: 

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "status": "OPEN",
  "due_date": "2023-12-08T15:59:52.487Z",
  "timestamp": "2023-12-08T15:59:52.487Z",
  "tags": [
    "string"
  ]
}
```

### 6. Partially Update Todo

#### Endpoint

- **Method**: PATCH
- **Path**: `/api/todos/{id}/`

#### Request

- **Parameters**:
  - `id` (integer) - A unique integer value identifying this todo.

#### Request Body

```json
{
  "title": "string",
  "description": "string",
  "status": "OPEN",
  "due_date": "2023-12-08T15:59:52.490Z",
  "tags": [
    "string"
  ]
}
```

#### Response

- **Status Code**: 200 OK
- **Body**: 

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "status": "OPEN",
  "due_date": "2023-12-08T15:59:52.495Z",
  "timestamp": "2023-12-08T15:59:52.495Z",
  "tags": [
    "string"
  ]
}
```

### 7. Delete Todo

#### Endpoint

- **Method**: DELETE
- **Path**: `/api/todos/{id}/`

#### Request

- **Parameters**:
  - `id` (integer) - A unique integer value identifying this todo.

#### Response

- **Status Code**: 204 No Content

---

