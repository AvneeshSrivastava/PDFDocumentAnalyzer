# PDF Document Analyzer

A production-ready **PDF Document Analyzer** built using **FastAPI**, **Jinja2**, **PyPDF**, and **Bootstrap 5** as part of the **AI ML Road Map**.

The application enables users to upload PDF documents, extract text, search keywords with highlighted results, and view document metadata through a responsive web interface.

---

# Features

* Upload PDF documents
* Extract text from PDF files
* Search keywords with highlighted results
* Display keyword occurrence count
* View PDF metadata

  * Total pages
  * File size
* PDF validation
* Global exception handling
* Centralized logging
* Responsive Bootstrap UI
* Health check endpoint
* Docker support

## Application Screenshots

### Home Page

![Home](docs/images/home.png)

### PDF Analysis Dashboard

![Dashboard](docs/images/result.png)

### Search Results

![Search](docs/images/search.png)

### Error Page

![Error](docs/images/error.png)

---

# Technology Stack

* Python 3.13
* FastAPI
* Jinja2
* PyPDF
* Bootstrap 5
* HTML5
* CSS3
* JavaScript
* Docker
* Git & GitHub

---

# Project Structure

```text
PDFDocumentAnalyzer/
│
├── data/
│   ├── input/
│   └── output/
│
├── logs/
│
├── src/
│   ├── config/
│   ├── exceptions/
│   ├── services/
│   ├── web/
│   │   ├── routes/
│   │   └── app.py
│   ├── logging.py
│   └── validators.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Application Architecture

```text
Browser
    │
    ▼
FastAPI Routes
    │
    ▼
Validation Layer
    │
    ▼
Service Layer
    │
    ├── File Service
    ├── PDF Service
    └── Search Service
    │
    ▼
Templates (Jinja2)
```

---

# Prerequisites

* Python 3.13+
* Git
* pip

(Optional)

* Docker Desktop

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```

Navigate to the project.

```bash
cd PDFDocumentAnalyzer
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Application

```bash
uvicorn src.app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

# Running with Docker

Build and start the application.

```bash
docker compose up --build
```

Application URL

```text
http://localhost:8000
```

---

# Available Endpoints

| Endpoint  | Method | Description            |
| --------- | ------ | ---------------------- |
| `/`       | GET    | Home page              |
| `/upload` | POST   | Upload and analyze PDF |
| `/search` | POST   | Search keyword         |
| `/health` | GET    | Health check           |

---

# Current Features

* PDF upload
* Text extraction
* Keyword search
* Search highlighting
* PDF metadata
* File validation
* Logging
* Exception handling
* Responsive UI
* Docker support

---

# Future Roadmap

* OCR support for scanned PDFs
* Export extracted text to DOCX
* Export search results
* Search history
* User authentication
* Database integration
* AI-powered document summarization
* Question answering over PDFs using RAG
* Semantic search using vector databases

---

# Screenshots

> Add application screenshots here after deployment.

---

# Git Workflow

```text
main
  │
develop
  │
feature/*
```

---

# Author

**Avneesh Srivastava**

---

# AI ML Road Map

This project is **Phase 1** of the **AI ML Road Map**, a structured learning journey toward becoming an **AI Engineer** through hands-on projects.

### Completed

* ✅ PDF Document Analyzer

### Upcoming Projects

* AI Resume Analyzer
* Software Architecture Knowledge Bot
* Bhagavad Gita Q&A Bot
* Interview Preparation Assistant
* Personal Productivity Agent
* Job Search Agent
* Multi-Agent Research Assistant
* AI Software Architect Assistant

---

# License

This project is intended for educational and portfolio purposes.