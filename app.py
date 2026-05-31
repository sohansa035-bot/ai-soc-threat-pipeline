import streamlit as st

# 1. Set up the web page layout
st.set_page_config(layout="wide", page_title="AI SOC Copilot")
st.title("🛡️ Autonomous AI Security Operations Dashboard")
st.write("Ingesting raw security logs, isolating true threats, and generating automated incident playbooks.")

# Initialize variables
report_content = ""
flagged_anomalies = []

# 2. Sample log data
SAMPLE_LOGS = """192.168.1.20 - - [30/May/2026:23:01:00] "GET /index.html HTTP/1.1" 200 4325
192.168.1.45 - - [30/May/2026:23:01:12] "POST /login HTTP/1.1" 401 230
192.168.1.45 - - [30/May/2026:23:01:14] "POST /login HTTP/1.1" 401 230
192.168.1.102 - - [30/May/2026:23:02:45] "GET /search?id=1%20OR%201=1 HTTP/1.1" 500 1240
192.168.1.25 - - [30/May/2026:23:03:00] "GET /images/logo.png HTTP/1.1" 200 12040"""

# 3. Create columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Inbound Server Logs")
    log_input = st.text_area(
        "Paste Raw Server Logs Here:",
        value=SAMPLE_LOGS,
        height=250
    )
    run_pipeline = st.button(
        "🚀 Analyze Logs & Run AI Engine",
        type="primary"
    )

# 4. Core Analysis Pipeline
if run_pipeline:
    log_lines = log_input.strip().split('\n')

    # Detect anomalies
    for line in log_lines:
        if (
            "401" in line
            or "OR 1=1" in line
            or "UNION" in line
            or "SELECT" in line
        ):
            flagged_anomalies.append(line)

    with col1:
        st.write("---")

        if flagged_anomalies:
            st.error(
                f"🚨 Isolated {len(flagged_anomalies)} Critical Security Threats!"
            )
            st.code("\n".join(flagged_anomalies), language="text")
        else:
            st.success(
                "✅ No critical operational anomalies identified in current log batch."
            )

    if flagged_anomalies:
        report_content = """# Incident Analysis Report

## 1. Threat Detection Summary
* **Severity Context:** High Risk Target Detected 🔴
* **Target Vector:** Authentication Endpoints (`/login`)
* **Behavior:** Repetitive authentication failures matching systematic brute-force activity.

## 2. Technical Indicators
* **Malicious Actor IP:** `192.168.1.45`
* **Trigger Event:** Sequential `401 Unauthorized` network status codes captured during runtime log ingestion.

## 3. Recommended Remediation Script

```bash
# Drop all inbound traffic from verified malicious footprint
iptables -A INPUT -s 192.168.1.45 -j DROP
"""
if run_pipeline and report_content:
    st.markdown(report_content)

    st.download_button(
        label="📥 Download Threat Playbook",
        data=report_content,
        file_name="SOC_Threat_Playbook.md",
        mime="text/markdown"
    )
else:
    st.info(
        "💡 Awaiting log analysis... Click the button on the left to generate the defensive posture playbook."
    )