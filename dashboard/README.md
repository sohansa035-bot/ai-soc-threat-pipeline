# AI-SOC Dashboard

This directory contains the Streamlit frontend application for the AI-SOC Threat Pipeline.

## Overview
The dashboard provides a visual interface for SOC analysts to:
1. Paste raw server logs for manual analysis.
2. View parsed anomalies and filtered threats in real-time.
3. Review AI-generated threat playbooks with confidence scores and recommended remediation commands.

## Running Locally

To run the dashboard independently (assuming the backend API is already running):

```bash
pip install -r ../requirements.txt
streamlit run app.py
```

By default, the dashboard expects the backend API to be running at `http://localhost:8000/analyze`. You can override this by setting the `API_URL` environment variable.
