# AI-Powered Location Finder API

## Overview

This project is a full-stack, containerized web application developed as a technical test. It allows users to find places (e.g., restaurants, cafes) by describing what they are looking for in natural language. The system leverages a local Large Language Model (LLM) to understand the user's intent and integrates with the Google Maps API to provide real-world location data, including embeddable maps and directions from the user's current location.

The entire architecture is built with best practices in mind, focusing on automation, integration logic, security, and a production-ready workflow.

---

## Key Features

-   **Natural Language Input**: Users can type requests like "sate padang terenak di blok m" instead of structured queries.
-   **AI-Powered Intent Extraction**: A locally-run `deepseek-r1:7b` model via Ollama parses the user's prompt to extract the "what" and "where".
-   **Google Maps Integration**: Fetches real-time location data, addresses, ratings, and generates links for directions and embedded maps.
-   **Geolocation-Aware Directions**: Provides driving directions from the user's current geographical location.
-   **Asynchronous Task Processing**: Uses Celery and Redis to handle long-running AI and API calls in the background, ensuring a non-blocking, responsive user experience.
-   **Fully Containerized**: The entire stack (Django, Gunicorn, PostgreSQL/PostGIS, Redis, Ollama, Celery Worker) is managed by Docker and Docker Compose for perfect reproducibility.
-   **Secure and Production-Ready**: Implements API rate limiting to prevent abuse, secure secrets management via environment variables, and uses a production-grade WSGI server (Gunicorn).

---

## Tech Stack & Architecture

-   **Backend**: Python, Django, Django REST Framework
-   **Database**: PostgreSQL + PostGIS
-   **AI Model**: Ollama with `deepseek-r1:7b`
-   **Task Queue & Broker**: Celery, Redis
-   **Frontend**: Vanilla HTML, CSS, and JavaScript
-   **DevOps & Deployment**: Docker, Docker Compose, Gunicorn

---

## Prerequisites

-   [Docker](https://www.docker.com/get-started)
-   [Docker Compose](https://docs.docker.com/compose/install/)
-   NVIDIA GPU with appropriate drivers and [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) (for GPU acceleration of the LLM).

---

## 🚀 Setup & Installation

**1. Clone the Repository**
```bash
git clone [Link ke Repository GitHub Anda]
cd [nama-folder-proyek]```

**2. Create the Environment File**
Create a `.env` file in the project root by copying the example file.
```bash
cp .env.example .env
```

**3. Add Your Google Maps API Key**
Open the newly created `.env` file and replace `"AIzaSy...YOUR_API_KEY_HERE"` with your actual Google Maps Platform API key.

**4. Build and Run the Application**
Use Docker Compose to build all the images and run the services. This command will start the web server, database, worker, Ollama, and all other components.

```bash
# This command might take a while on the first run as it needs to
# download base images and pull the LLM model.
docker-compose -f docker-compose.prod.yml up --build
```
The application will be running and accessible at `http://localhost:8000`.

*(For a development environment with hot-reloading, you can use the standard `docker-compose up --build` command.)*

---

## How to Use

Once the containers are running, simply open your web browser and navigate to:

`http://localhost:8000`

Your browser will ask for permission to access your location. Allow it for the best experience. Type what you are looking for into the search box and click "Cari". The results will appear on the page asynchronously.````

---
