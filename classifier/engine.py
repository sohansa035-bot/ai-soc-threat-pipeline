from typing import List
from urllib.parse import unquote
from models.schemas import Alert

class ThreatClassifier:
    def __init__(self):
        pass

    def classify_and_score(self, anomalies: List[str]) -> List[Alert]:
        """
        Analyze isolated anomalies and generate automated threat alerts.
        In a production setting, this would call an LLM (e.g., OpenAI).
        """
        if not anomalies:
            return []

        # Stubbed implementation based on the original app.py logic
        alerts = []
        decoded_anomalies = [unquote(a) for a in anomalies]
        
        # Check if it looks like a brute force or SQLi
        has_auth_fail = any("401" in a for a in decoded_anomalies)
        has_sqli = any(kw in a for a in decoded_anomalies for kw in ["OR 1=1", "UNION", "SELECT"])

        if has_auth_fail:
            alerts.append(Alert(
                severity="High",
                attack_type="Brute Force",
                confidence=96,
                recommended_action="iptables -A INPUT -s [ATTACKER_IP] -j DROP",
                technical_indicators=["Sequential 401 Unauthorized codes detected"]
            ))
            
        if has_sqli:
            alerts.append(Alert(
                severity="Critical",
                attack_type="SQL Injection",
                confidence=98,
                recommended_action="Block IP, sanitize input parameters",
                technical_indicators=["SQL syntax injected in URL parameters"]
            ))

        return alerts
