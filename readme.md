# Job Search Agent

## Overview

Job Search Agent is an AI-powered backend service that analyzes a user's resume and automatically discovers relevant job opportunities from LinkedIn. The system uses a combination of natural language processing, vector embeddings, and automated web scraping to identify the most relevant and recently posted jobs.

The application processes a resume, extracts meaningful skills and keywords using a large language model (LLM), and searches LinkedIn for matching job postings. The results are returned in a structured format that can be downloaded as either CSV or JSON.

This project is designed as a **production-ready backend service** built with a modular architecture and containerization support.

---

## Key Capabilities

### Resume Understanding

The system parses a user's uploaded resume and extracts the raw text. The text is then segmented into chunks and converted into vector embeddings for semantic processing.

### Skill and Keyword Extraction

An LLM analyzes the resume text to identify the most relevant technical skills, job roles, and domain keywords. These keywords drive the job search process.

### Vector Storage

The resume embeddings are stored in a vector database to support semantic operations and future enhancements such as resume-job matching and ranking.

### Automated Job Discovery

The application uses a Playwright-based scraping engine with a Chromium browser to search LinkedIn job listings. It collects the most recent jobs related to the extracted keywords.

### Proxy-Based Scraping

To improve reliability and avoid scraping restrictions, the system rotates residential proxies during job discovery.

### Structured Job Results

Job listings are returned in a structured dataset containing:

* source
* title
* company
* location
* date_posted
* job_type
* url
* about

Users can download results as either CSV or JSON.

---

## System Architecture

The project follows an agent-based workflow orchestrated through LangGraph.

```
User Request
     │
     ▼
FastAPI API
     │
     ▼
LangGraph Workflow
     │
     ├── Resume Parsing
     │
     ├── Resume Chunking
     │
     ├── Embedding Generation
     │
     ├── Vector Storage (Pinecone)
     │
     ├── Keyword Extraction (LLM)
     │
     ▼
Job Search Engine
     │
     ├── Playwright + Chromium
     ├── LinkedIn Job Search
     ├── Proxy Rotation
     │
     ▼
Structured Job Results
     │
     ▼
CSV / JSON Download
```

---

## Project Structure

```
resume_agent/
│
├── agents/
│   └── job_agent.py
│
├── graph/
│   └── workflow.py
│
├── scraper/
│   └── job_scraper.py
│
├── rag/
│   ├── embedder.py
│   └── vector_store.py
│
├── utils/
│   └── resume_parser.py
│
├── llm/
│   └── keyword_extractor.py
│
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## API Endpoint

### Search Jobs

```
POST /search-jobs
```

### Request Parameters

| Parameter     | Type   | Description |
| ------------- | ------ | ----------- |
| resume        | File   | Resume PDF  |
| output_format | string | csv or json |

### Example Request

```
POST /search-jobs
Content-Type: multipart/form-data

resume = resume.pdf
output_format = csv
```

### Response

A downloadable file containing structured job data.

Example CSV output:

```
source,title,company,location,date_posted,job_type,url,about
linkedin_job,AI/ML Engineer,BayOne Solutions,India,23 minutes ago,On-site,https://...,AI/ML Engineer role at BayOne Solutions located in India
```

---

## Environment Configuration

The application requires the following environment variables.

```
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_llm_api_key
PROXY_USERNAME=your_proxy_username
PROXY_PASSWORD=your_proxy_password
```

These variables should be configured before starting the application.

---

## Running the Application Locally

### 1. Clone the Repository

```
git clone <repository_url>
cd resume_agent
```

### 2. Create a Virtual Environment

```
python -m venv venv
```

Activate the environment.

Windows:

```
venv\Scripts\activate
```

Linux or Mac:

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

Install Playwright browser dependencies.

```
playwright install chromium
```

### 4. Start the API Server

```
uvicorn main:app --reload
```

The server will start at:

```
http://localhost:8000
```

Interactive API documentation is available at:

```
http://localhost:8000/docs
```

---

## Output Data Schema

The API returns structured job information with the following fields:

| Field       | Description                         |
| ----------- | ----------------------------------- |
| source      | Job platform source                 |
| title       | Job title                           |
| company     | Company offering the role           |
| location    | Job location                        |
| date_posted | Time since job was posted           |
| job_type    | Work format (On-site, Remote, etc.) |
| url         | Direct link to the job posting      |
| about       | Short summary of the role           |

---

## Production Considerations

This application is designed to run as a containerized backend service and supports the following production features:

* Stateless API architecture
* Proxy rotation for scraping stability
* Modular agent-based workflow
* Vector database integration
* Structured data export
* Containerized deployment support
* Separation of scraping, AI processing, and API layers

The architecture allows easy scaling and integration into larger job discovery or recruitment platforms.

---

## Potential Extensions

Future improvements may include:

* Multi-platform job aggregation
* Resume-to-job similarity ranking
* Real-time job alerts
* Job recommendation scoring
* Distributed scraping pipelines
* Async job processing

---

## License

This project is intended for educational and research purposes. When using scraping functionality, ensure compliance with the terms of service of the target platforms.

---

## Author

AI-powered job discovery system built using agent-based architecture, vector search, and automated web scraping.
