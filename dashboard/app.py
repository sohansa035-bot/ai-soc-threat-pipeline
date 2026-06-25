import streamlit as st
import requests
import json
import os

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000/analyze")

st.set_page_config(layout="wide", page_title="AI SOC Copilot")
st.title("🛡️ Autonomous AI Security Operations Dashboard")
st.write("Ingesting raw security logs, isolating true threats, and generating automated incident playbooks.")

SAMPLE_LOGS = """192.168.1.20 - - [30/May/2026:23:01:00] "GET /index.html HTTP/1.1" 200 4325
192.168.1.45 - - [30/May/2026:23:01:12] "POST /login HTTP/1.1" 401 230
192.168.1.45 - - [30/May/2026:23:01:14] "POST /login HTTP/1.1" 401 230
192.168.1.102 - - [30/May/2026:23:02:45] "GET /search?id=1%20OR%201=1 HTTP/1.1" 500 1240
192.168.1.25 - - [30/May/2026:23:03:00] "GET /images/logo.png HTTP/1.1" 200 12040"""

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Inbound Server Logs")
    log_input = st.text_area("Paste Raw Server Logs Here:", value=SAMPLE_LOGS, height=250)
    run_pipeline = st.button("🚀 Analyze Logs & Run AI Engine", type="primary")

if run_pipeline:
    log_lines = [line.strip() for line in log_input.strip().split('\n') if line.strip()]
    
    with st.spinner("Analyzing via AI-SOC Backend..."):
        try:
            response = requests.post(API_URL, json={"logs": log_lines})
            response.raise_for_status()
            data = response.json()
            
            with col1:
                st.write("---")
                if data["threats_detected"] > 0:
                    st.error(f"🚨 Isolated {data['threats_detected']} Critical Security Threats!")
                    st.code("\n".join(data["raw_anomalies"]), language="text")
                else:
                    st.success("✅ No critical operational anomalies identified.")
            
            with col2:
                if data["alerts"]:
                    st.subheader("🤖 Generated Threat Intelligence")
                    for idx, alert in enumerate(data["alerts"]):
                        with st.expander(f"Incident: {alert['attack_type']} ({alert['severity']})", expanded=True):
                            st.write(f"**Confidence Score:** {alert['confidence']}%")
                            st.write("**Technical Indicators:**")
                            for ind in alert['technical_indicators']:
                                st.write(f"- {ind}")
                            st.code(alert['recommended_action'], language="bash")
                else:
                    st.info("No actionable alerts generated.")
                    
        except requests.exceptions.RequestException as e:
            st.error(f"Connection to backend failed. Is the API running at {API_URL}? Error: {str(e)}")
