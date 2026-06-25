---
title: AI-SOC Threat Pipeline
emoji: 🛡️
colorFrom: red
colorTo: yellow
sdk: docker
pinned: false
---

# 🛡️ AI-SOC Threat Pipeline

> **AI-Powered Threat Detection • Correlation • Incident Response**

[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)]()
[![Lint](https://github.com/sohansa035-bot/ai-soc-threat-pipeline/actions/workflows/lint.yml/badge.svg)](https://github.com/sohansa035-bot/ai-soc-threat-pipeline/actions/workflows/lint.yml)
[![Tests](https://github.com/sohansa035-bot/ai-soc-threat-pipeline/actions/workflows/test.yml/badge.svg)](https://github.com/sohansa035-bot/ai-soc-threat-pipeline/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Supported-green.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-red.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **AI-SOC Threat Pipeline is an intelligent Security Operations Center (SOC) platform that automates log analysis, threat detection, incident correlation, and response recommendations using AI. It helps reduce analyst workload and improves response time by transforming raw security events into actionable insights.**

## 📖 Overview

### The Problem

Security teams receive thousands of alerts every day.

Most alerts are:
- False positives
- Duplicate alerts
- Low priority
- Time-consuming to investigate

Manual analysis slows down incident response and increases Mean Time to Respond (MTTR).

### The Solution

AI-SOC Threat Pipeline combines:
- AI-assisted log analysis
- Threat classification
- Alert correlation
- Automated incident reports
- Response recommendations

to help SOC analysts investigate incidents faster.

### ✨ Key Features

- AI-powered log analysis
- Threat intelligence correlation
- Alert prioritization
- Incident timeline generation
- MITRE ATT&CK mapping
- Risk scoring
- Automated reports
- Dashboard
- REST API

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[Firewall / IDS / EDR Logs] --> B[Log Parser]
    B --> C[Threat Intelligence Engine]
    C --> D[AI Analysis Engine]
    D --> E[Threat Classification]
    E --> F[Risk Scoring]
    F --> G[Incident Timeline]
    G --> H[Dashboard]
    G --> I[Automated Report]
```

---

## 🎯 Threat Processing Flow

```text
Incoming Logs
      ↓
Normalization
      ↓
Threat Correlation
      ↓
AI Classification
      ↓
Risk Score
      ↓
Incident Report
      ↓
SOC Analyst
```

---

## 💻 Tech Stack

- **Backend & Visualization:** Python, Streamlit
- **AI Integration:** OpenAI
- **Deployment:** Docker

---

<!-- Uncomment when assets are ready
## 📸 Screenshots

### Dashboard
![Dashboard](assets/dashboard.png)

### Threat Timeline
![Threat Timeline](assets/threat_timeline.png)

### Alert Panel
![Alert Panel](assets/alert_panel.png)

### Incident Report
![Incident Report](assets/incident_report.png)

### Risk Score
![Risk Score](assets/risk_score.png)

### Charts
![Charts](assets/charts.png)

---

## 🎥 Demo GIF

### Incident Resolution Flow (Demo)
![Demo GIF](assets/demo.gif)

*Receive Log → AI Analysis → Threat Classification → Dashboard → Generated Report*
-->

---

## 📊 Example Output

```json
{
  "severity": "High",
  "attack_type": "Brute Force",
  "confidence": 96,
  "recommended_action": "Block IP"
}
```

---



## 🛠️ Engineering Trade-offs

**Why FastAPI?**
- Future REST integration and standardized HTTP endpoints.
- Async support for high-throughput log ingestion.

**Why Streamlit?**
- Rapid prototyping for data applications.
- Minimal frontend overhead for deploying operational dashboards.

**Why Docker?**
- Portable deployments across different environments.
- Ensures reproducibility for the API and Dashboard.

**Why AI Classification?**
- Reduces SOC analyst workload.
- Improves incident prioritization through intelligent scoring.

---

## 📁 Folder Structure

```text
ai-soc-threat-pipeline/
├── api/
│   ├── __init__.py
│   └── main.py
├── classifier/
│   ├── __init__.py
│   └── engine.py
├── parser/
│   ├── __init__.py
│   └── log_parser.py
├── models/
│   ├── __init__.py
│   └── schemas.py
├── dashboard/
│   └── app.py
├── sample_logs/
├── tests/
├── .github/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🗺️ Roadmap

- [x] Log Parser
- [x] Threat Classification
- [x] Dashboard
- [x] Docker
- [ ] Multi-Agent Detection
- [ ] SIEM Integration
- [ ] Live Threat Feed
- [ ] SOAR Integration
- [ ] Cloud Deployment

---

## 🤝 Contributing

1. Fork the repository
2. Clone locally
3. Create a feature branch
4. Commit your changes
5. Submit a Pull Request

---

## 📄 License

[MIT](LICENSE)