# KeepUp Inventory Management System

[svg](https://github.com/VidhiDixit2000/fast-api-project#react--fastapi--postgresql-crud-application)

A full-stack CRUD application built with **React**, **FastAPI**, and **PostgreSQL**, containerized with **Docker**, deployed on **AWS EC2**, and hosted with the React frontend on **Netlify**.

This project was built primarily to understand and demonstrate practical **Docker, container networking, cloud deployment, environment variables, and frontend/backend deployment**.

---

## 🚀 Project Overview

[svg](https://github.com/VidhiDixit2000/fast-api-project#-project-overview)

The application provides a simple interface for managing product inventory:

- Create a product
- View all products
- View a product by ID
- Update a product
- Delete a product

### Tech Stack

[svg](https://github.com/VidhiDixit2000/fast-api-project#tech-stack)

Layer Technology

---

Frontend React Backend Python + FastAPI Database PostgreSQL ORM SQLAlchemy Containerization Docker + Docker Compose Backend Hosting AWS EC2 Frontend Hosting Netlify Version Control Git + GitHub

---

## 🏗️ Architecture

[svg](https://github.com/VidhiDixit2000/fast-api-project#%EF%B8%8F-architecture)

```
                         Internet
                            |
                 +----------+----------+
                 |                     |
                 v                     v
          Netlify (React)       AWS EC2 Server
                                      |
                                      v
                              FastAPI Container
                                      |
                                      v
                             PostgreSQL Container

```

**svg**

### Request Flow

[svg](https://github.com/VidhiDixit2000/fast-api-project#request-flow)

```
User
  |
  v
React Frontend (Netlify)
  |
  | HTTP API Request
  v
FastAPI API (AWS EC2 :8000)
  |
  v
PostgreSQL (Docker)

```

**svg**

The React application communicates with the FastAPI backend through the backend's API URL.

Inside Docker Compose, FastAPI communicates with PostgreSQL using the PostgreSQL service name (`postgres-db`) rather than `localhost`.

---

## 📁 Project Structure

[svg](https://github.com/VidhiDixit2000/fast-api-project#-project-structure)

```
project-root/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── ...
│   ├── public/
│   ├── package.json
│   ├── .env.development
│   ├── .env.production
│   └── ...
│
├── docker-compose.yml
└── README.md

```

**svg**

---

## ⚙️ Backend

[svg](https://github.com/VidhiDixit2000/fast-api-project#%EF%B8%8F-backend)

The backend is implemented using FastAPI.

Example API endpoints:

```
GET    /products
POST   /products
GET    /products/{id}
PUT    /products/{id}
DELETE /products/{id}

```

**svg**

FastAPI provides the REST API, while SQLAlchemy is used to interact with PostgreSQL.

---

## 🗄️ Database

[svg](https://github.com/VidhiDixit2000/fast-api-project#%EF%B8%8F-database)

The project uses PostgreSQL.

When running locally without Docker, the database can be accessed through `localhost`.

When FastAPI and PostgreSQL are running in Docker Compose, the backend connects to PostgreSQL through the Docker Compose service name:

```
postgres-db

```

**svg**

Example Docker database URL:

```
postgresql://postgres:<PASSWORD>@postgres-db:5432/postgres

```

**svg**

The application reads the database connection string from an environment variable:

```
import os

DATABASE_URL = os.getenv("DATABASE_URL")
```

**svg**

This keeps database configuration outside the application code.

---

## 🐳 Docker

[svg](https://github.com/VidhiDixit2000/fast-api-project#-docker)

The backend and PostgreSQL database are containerized.

### Build and start the application

[svg](https://github.com/VidhiDixit2000/fast-api-project#build-and-start-the-application)

```
docker compose up --build
```

**svg**

### Start existing images

[svg](https://github.com/VidhiDixit2000/fast-api-project#start-existing-images)

```
docker compose up -d
```

**svg**

### Check running containers

[svg](https://github.com/VidhiDixit2000/fast-api-project#check-running-containers)

```
docker ps
```

**svg**

### Stop the containers

[svg](https://github.com/VidhiDixit2000/fast-api-project#stop-the-containers)

```
docker compose down
```

**svg**

### View logs

[svg](https://github.com/VidhiDixit2000/fast-api-project#view-logs)

```
docker compose logs
```

**svg**

For the FastAPI service:

```
docker compose logs fastapi
```

**svg**

---

## 🔌 Docker Networking

[svg](https://github.com/VidhiDixit2000/fast-api-project#-docker-networking)

One important Docker concept used in this project is **service-to-service communication**.

The FastAPI container does **not** use:

```
localhost

```

**svg**

to reach PostgreSQL.

Instead, Docker Compose provides internal DNS, so the PostgreSQL service can be reached using:

```
postgres-db

```

**svg**

Therefore:

```
FastAPI Container
       |
       | DATABASE_URL
       v
postgres-db:5432

```

**svg**

This is different from accessing PostgreSQL from the host machine, where `localhost:5432` may be used.

---

## 💻 Running Locally

[svg](https://github.com/VidhiDixit2000/fast-api-project#-running-locally)

### 1. Start PostgreSQL and FastAPI

[svg](https://github.com/VidhiDixit2000/fast-api-project#1-start-postgresql-and-fastapi)

From the project root:

```
docker compose up --build
```

**svg**

The FastAPI API is available at:

```
http://localhost:8000

```

**svg**

FastAPI's interactive API documentation is available at:

```
http://localhost:8000/docs

```

**svg**

### 2. Start the React frontend

[svg](https://github.com/VidhiDixit2000/fast-api-project#2-start-the-react-frontend)

Navigate to the frontend:

```
cd frontend
```

**svg**

Install dependencies:

```
npm install
```

**svg**

Start the development server:

```
npm start
```

**svg**

If port `3000` is already occupied, React can run on another port such as:

```
http://localhost:3001

```

**svg**

---

## 🌐 Frontend Environment Variables

[svg](https://github.com/VidhiDixit2000/fast-api-project#-frontend-environment-variables)

The frontend uses an environment variable to determine where the backend API is hosted.

### Development

[svg](https://github.com/VidhiDixit2000/fast-api-project#development)

`.env.development`

```
REACT_APP_API_URL=http://127.0.0.1:8000
```

**svg**

### Production

[svg](https://github.com/VidhiDixit2000/fast-api-project#production)

`.env.production`

```
REACT_APP_API_URL=http://<EC2_PUBLIC_IP>:8000
```

**svg**

The React application accesses it using:

```
process.env.REACT_APP_API_URL
```

**svg**

This allows the same frontend codebase to communicate with different backend environments.

---

## ☁️ AWS EC2 Deployment

[svg](https://github.com/VidhiDixit2000/fast-api-project#%EF%B8%8F-aws-ec2-deployment)

The FastAPI backend was deployed to an **AWS EC2** instance.

The deployment flow was:

```
Local Project
     |
     v
GitHub
     |
     v
AWS EC2
     |
     v
Docker
     |
     +------ FastAPI Container
     |
     +------ PostgreSQL Container

```

**svg**

### EC2 Setup

[svg](https://github.com/VidhiDixit2000/fast-api-project#ec2-setup)

The EC2 server runs Docker and Docker Compose.

After connecting to the server:

```
docker ps
```

**svg**

The FastAPI application is exposed on port:

```
8000

```

**svg**

The API can then be accessed through the EC2 public IP:

```
http://<EC2_PUBLIC_IP>:8000

```

**svg**

FastAPI documentation:

```
http://<EC2_PUBLIC_IP>:8000/docs

```

**svg**

> Replace `<EC2_PUBLIC_IP>` with the current public IP of your EC2 instance. Avoid committing a changing EC2 IP directly into source code.

---

## 🔐 AWS Security Group

[svg](https://github.com/VidhiDixit2000/fast-api-project#-aws-security-group)

The EC2 security group needs to allow the required inbound traffic.

Typical development configuration:

Protocol Port Purpose

---

SSH 22 Server administration TCP 8000 FastAPI API

For a production deployment, access rules should be restricted appropriately rather than exposing development ports publicly.

---

## 🌍 Netlify Frontend Deployment

[svg](https://github.com/VidhiDixit2000/fast-api-project#-netlify-frontend-deployment)

The React frontend was deployed using **Netlify**.

Netlify configuration:

```
Branch: main
Base directory: frontend
Build command: npm run build
Publish directory: build

```

**svg**

The production frontend uses the EC2 backend URL through:

```
REACT_APP_API_URL=http://<EC2_PUBLIC_IP>:8000
```

**svg**

After the frontend is deployed, the user accesses the React application through the production Netlify URL:

**Live Application:** https://keepupinventory.netlify.app/

---

## 🔄 Complete Deployment Flow

[svg](https://github.com/VidhiDixit2000/fast-api-project#-complete-deployment-flow)

```
                 GitHub Repository
                         |
              +----------+----------+
              |                     |
              v                     v
          Netlify                 AWS EC2
        React Build             Docker Compose
              |                     |
              |                     +--> FastAPI
              |                     |
              |                     +--> PostgreSQL
              |                     |
              +-------- HTTP -------+

```

**svg**

The deployed architecture separates the frontend and backend:

- **Frontend:** React application hosted on **Netlify**
- **Backend:** FastAPI application running in a Docker container on **AWS EC2**
- **Database:** PostgreSQL running in Docker on the EC2 server
- **Communication:** React frontend communicates with the FastAPI backend over HTTP

A typical user request looks like:

```
Browser
   |
   v
React App on Netlify
   |
   | GET /products
   v
FastAPI on EC2
   |
   v
PostgreSQL Container
   |
   v
Products Data
   |
   v
FastAPI Response
   |
   v
React UI

```

**svg**

---

## 🧪 Testing the Backend

[svg](https://github.com/VidhiDixit2000/fast-api-project#-testing-the-backend)

You can verify that FastAPI is running with:

```
curl http://localhost:8000/products
```

**svg**

You can also open:

```
/docs

```

**svg**

to use FastAPI's Swagger UI and test the API interactively.

---

## 🛠️ Troubleshooting

[svg](https://github.com/VidhiDixit2000/fast-api-project#%EF%B8%8F-troubleshooting)

### CORS Error

[svg](https://github.com/VidhiDixit2000/fast-api-project#cors-error)

If the React frontend is running on a different origin, FastAPI needs to allow the frontend origin.

For example:

```
Frontend:
http://localhost:3001

Backend:
http://localhost:8000

```

**svg**

These are different origins, so CORS must be configured appropriately in FastAPI.

---

### PostgreSQL Connection Error

[svg](https://github.com/VidhiDixit2000/fast-api-project#postgresql-connection-error)

Inside Docker, make sure the database hostname is:

```
postgres-db

```

**svg**

and not:

```
localhost

```

**svg**

For example:

```
DATABASE_URL=postgresql://postgres:<PASSWORD>@postgres-db:5432/postgres
```

**svg**

---

### Port Already in Use

[svg](https://github.com/VidhiDixit2000/fast-api-project#port-already-in-use)

If port `3000` is already occupied, React may ask to use another port such as `3001`.

For FastAPI, check whether port `8000` is already being used:

```
docker ps
```

**svg**

---

## 📌 Key Concepts Demonstrated

[svg](https://github.com/VidhiDixit2000/fast-api-project#-key-concepts-demonstrated)

This project demonstrates practical experience with:

- React frontend development
- REST API development with FastAPI
- PostgreSQL database integration
- SQLAlchemy
- CRUD operations
- Environment variables
- CORS
- Dockerfiles
- Docker Compose
- Docker networking
- Containerized PostgreSQL
- AWS EC2 deployment
- Linux server basics
- Netlify frontend deployment
- Git/GitHub-based workflow
- Debugging deployed applications

---

## 🎯 Learning Objective

[svg](https://github.com/VidhiDixit2000/fast-api-project#-learning-objective)

The main goal of this project was not to build a complex business application, but to understand how a modern application moves from local development to a cloud-hosted environment.

The progression was:

```
Application Development
        ↓
React + FastAPI + PostgreSQL
        ↓
Docker
        ↓
Docker Compose
        ↓
AWS EC2
        ↓
Netlify
        ↓
Deployed Full-Stack Application

```

**svg**

This provides a foundation for adding more advanced DevOps practices later, such as CI/CD with GitHub Actions, container registries, infrastructure as code, monitoring, and Kubernetes.