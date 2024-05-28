# Python - Automatic  Database Migrations

This repository provides a solution for settingup automatic database migrations using python alembic with FastAPI project, Docker and PostgreSQL.

## Prerequisites

- Docker installed on your machine. You can download it [here](https://www.docker.com/get-started).
- Docker Compose (typically included with Docker Desktop installations).

##  Team Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone <repository_url>
    ```



2. Create a vertual envernment for the project and activateit :

    ```bash
    python -m venv .myvenv
    source source .myvenv/bin/activate
    ```

3. Navigate to the project directory:

    ```bash
    cd fblueskye_test_assingnment
    ```

4. Build and run the Docker containers:

    ```bash
    docker-compose up--build -d
    ```

5. Access the PostgreSQL database using a database management tool such as pgAdmin or docker exec -it cmd:

    ```
    Host: localhost
    Port: 5432
    Username: root
    Password: root
    ```

    ```
    docker exec -it <psql_cointer_id> /bin/bash

    psql test_db
    ```
6. Access the FastAPI application in your web browser:

    ```
    http://localhost:8000/docs
    ```



