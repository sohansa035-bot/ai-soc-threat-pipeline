# 🛡️ Autonomous AI Security Operations & Threat Pipeline
### Project Submission for Codorra 2026

## 🚀 The Problem
Security Operations Center (SOC) analysts are completely drowning in massive amounts of daily logs. Manual log triage takes hours per incident, making it incredibly difficult to separate background noise from active system attacks. This causes severe analyst burnout and critical delays in threat remediation.

## 💡 The Solution
This project introduces an **Autonomous AI Security Operations Dashboard** that transforms a manual human triage process into an automated workflow:
1. **Log Ingestion & Filtering:** High-speed heuristic rules parse inbound raw server traffic to screen out normal background entries and instantly isolate high-priority threat clusters (such as Brute Force attempts).
2. **Automated Incident Playbook Engine:** Passes the isolated anomalies to a specialized template core to instantly generate an enterprise-grade threat playbook detailing the Threat Detection Summary, Technical Indicators, and an executable firewall remediation script.

## 🛠️ Tech Stack & Devops Architecture
* **Frontend Dashboard:** Streamlit (Pure Python Data Interface)
* **Log Parser Engine:** Native Python string evaluation and filtering arrays
* **Deployment Blueprint:** Production-ready `Dockerfile` and `docker-compose.yml` for isolated container deployment.

## 🏃‍♂️ How to Run Locally

### 1. Run via Local Python Environment
Open your terminal in the project directory and run:
```bash
pip install -r requirements.txt
streamlit run app.py