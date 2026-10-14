# 🏦 MonarchCredit – AI Powered Alternate Credit Scoring System

🚀 Built for **Barclays Hack-O-Hire 2026**

MonarchCredit is an AI-powered alternate credit scoring platform designed to enable **financial inclusion** by evaluating the creditworthiness of **unbanked and underbanked individuals as well as MSMEs**, beyond traditional CIBIL-based systems.

---

## 📌 Problem Statement

Millions of individuals and MSMEs lack formal credit histories, making them invisible to traditional credit scoring systems. As a result, many creditworthy applicants are denied access to fair lending opportunities. MonarchCredit addresses this gap by using alternative financial signals, machine learning, and explainable AI to assess creditworthiness more inclusively and transparently.

👉 MonarchCredit solves this by:
- Leveraging **behavioral financial data**
- Using **AI-driven risk assessment**
- Providing **transparent and explainable decisions**

---

## 💡 Solution Overview

The system processes structured financial data (simulating Account Aggregator flows) and generates:

- 📊 **Risk Score**
- 💳 **CIBIL-style Credit Score**
- ✅ **Loan Approval / Rejection Decision**
- 💰 **Suggested Loan Terms (Principal & Interest Rate)**

---

## 🧠 Key Features

### 🔹 Dual AI Models
- Separate models for:
  - **Individuals**
  - **MSMEs**
- Tailored features and signals for each segment

---

### 🔹 Responsible Data Processing
- Removes **protected attributes** (gender, religion, etc.)
- Evaluates potential fairness concerns in model decisions

---

### 🔹 Advanced Feature Engineering
- Raw data is transformed into **handcrafted features**
- Captures:
  - Income stability
  - Financial behavior
  - Asset-liability balance
  - Social and behavioral signals

---

### 🔹 Ensemble ML Decision Engine
Built using:
- **XGBoost**
- **Random Forest**
- **LightGBM**

👉 Outputs:
- Risk score
- Loan decision
- Suggested interest rate & principal

---

### 🔹 Explainable AI (SHAP)
- Provides feature-level explanations for model predictions
- Helps reviewers inspect factors contributing to an applicant's score

---

### 🔹 Human-in-the-Loop System
- Managers can:
  - Accept model decisions
  - Override decisions when necessary

---

### 🔹 Dual User Interfaces

#### 👤 Customer Interface
- Upload financial JSON (Account Aggregator simulation)
- View:
  - Credit score
  - Decision
  - Personalized report

#### 🧑‍💼 Manager Interface
- Review applications
- View SHAP explanations
- Override decisions
- Generate reports

---

### 🔹 Automated PDF Reports
- Customer report
- Manager report

Includes:
- Decision summary
- Risk insights
- Loan details
- Explanation

---

### 🔹 AI Chatbot 🤖
An assistant designed to:
- Explain why an applicant was rejected
- Compare multiple applicants
- Help customers understand their reports
- Assist managers with decision insights
- Answer finance-related queries

---

### 🔹 Event-Driven Architecture (Kafka)

The project includes an Apache Kafka-based messaging setup intended to support event-driven processing between services.

- Asynchronous message processing
- Loose coupling between services
- Kafka topics for service communication

Actual reliability and data-loss guarantees depend on Kafka configuration, consumer behaviour, and service implementation.

---

### 🔹 Audit Trail & Compliance
The project includes audit-related components for tracking information such as:
- Customer data
- Model outputs
- Manager decisions
- Governance metadata

The presence of these components does not by itself establish regulatory compliance.

---

### 🔹 Feature Store (Future Scope)
Engineered features could be stored for:
- Future model retraining
- Model monitoring and improvement

---

## 🏗️ System Architecture

<p align="center">
  <img src="assets/system_architecture.png" width="900" alt="MonarchCredit system architecture"/>
</p>

The architecture diagram illustrates the project's intended service flow and Kafka-based messaging design.

---

## 📸 Demo & Screenshots

### 👤 Customer Flow

#### 🏠 Customer Dashboard
<p align="center">
  <img src="assets/customer_dashboard.png" width="800" alt="Customer dashboard"/>
</p>

#### 📤 Upload Financial Data
<p align="center">
  <img src="assets/customer_uploading.png" width="800" alt="Customer financial data upload"/>
</p>

#### ⏳ Processing & Evaluation
<p align="center">
  <img src="assets/customer_processingpage.png" width="800" alt="Customer processing and evaluation"/>
</p>

---

### 🧑‍💼 Manager Flow

#### 📊 Manager Dashboard
<p align="center">
  <img src="assets/manager_dashboard.png" width="800" alt="Manager dashboard"/>
</p>

#### 🧾 Decision & Underwriting Page
<p align="center">
  <img src="assets/manager_decisionpage.png" width="800" alt="Manager decision and underwriting page"/>
</p>

---

### 🤖 AI Chatbot

<p align="center">
  <img src="assets/chatbot.png" width="800" alt="MonarchCredit chatbot"/>
</p>

---

## ⚙️ Tech Stack

### 🔹 Backend
- FastAPI
- Kafka
- Python

### 🔹 Machine Learning
- XGBoost
- Random Forest
- LightGBM
- SHAP

### 🔹 Frontend
- React.js

### 🔹 Infrastructure
- Docker
- ChromaDB

---

## 💻 Local Setup (Windows)

### Prerequisites

Install Git, Python 3.12, Node.js, and Docker Desktop. Start Docker Desktop before launching the backend services.

### 1. Clone the repository

```powershell
git clone https://github.com/Rishi-1612/AI-credit-scoring-system.git
cd AI-credit-scoring-system
```

### 2. Configure environment variables

```powershell
Copy-Item alternate_credit_backend/.env.example alternate_credit_backend/.env
notepad alternate_credit_backend/.env
```

Set `DB_PASSWORD` and `MYSQL_PASSWORD` to a local development password (use the same value initially). Do not commit `alternate_credit_backend/.env`.

### 3. Start MySQL and Kafka

```powershell
cd alternate_credit_backend
docker compose config
docker compose up -d
docker compose ps
```

Wait until MySQL and Kafka are healthy. To inspect startup logs:

```powershell
docker compose logs --tail 100 mysql kafka kafka-init
```

### 4. Install backend dependencies

Keep this terminal in `alternate_credit_backend`:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m scripts.init_auth_db
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Bypass` in that terminal, then activate the environment again.

### 5. Start the API

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Check these URLs:
- API health: http://127.0.0.1:8000/
- Interactive API docs: http://127.0.0.1:8000/docs

The health endpoint should return `{"status":"ok","message":"API is running"}`.

### 6. Start the frontend

Open a second PowerShell terminal from the repository root:

```powershell
cd AI-credit-scoring-system\alternate_credit_frontend
npm install
npm run dev
```

Open the local URL printed by Vite (normally http://localhost:5173).

### Optional: Chatbot

The chatbot is a separate API on port 8999 and requires a Groq API key. Add `GROQ_API_KEY=your_key_here` to your local `alternate_credit_backend/.env`, then, in a separate terminal:

```powershell
cd AI-credit-scoring-system\alternate_credit_backend
.\.venv\Scripts\Activate.ps1
pip install -r chatbot/requirements.txt
pip install groq
cd chatbot
python app_chaty.py
```

### Current setup limitations

- The Compose file provides local MySQL and Kafka infrastructure. The auth initialization script creates the authentication `users` table.
- The application also queries project-specific MySQL tables such as `individual_manager_review_data`, `msme_manager_review_data`, `msme_final_decision`, and raw SHAP tables. Their complete MySQL DDL/migrations are not currently included in this repository, so dashboard and application-submission flows may still need schema initialization.
- Kafka scoring, explainability, and PDF workers are separate Python processes. The API's health endpoint verifies the web API, not that every background worker or full scoring flow is running.

## 📄 License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the **MIT License** © 2026 Aryan Phanse.

See the full license here: [LICENSE](./LICENSE)

---

## 📌 Project Notes

- Account Aggregator inputs are simulated rather than connected to a live financial-data provider.
- Model outputs depend on the available data, feature processing, and trained model artifacts.
- This repository is a project implementation and should not be treated as a production lending or regulatory-compliance system without further validation.
