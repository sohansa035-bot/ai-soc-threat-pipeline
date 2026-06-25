from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from models.schemas import LogBatch, AnalysisReport
from parser.log_parser import LogParser
from classifier.engine import ThreatClassifier

app = FastAPI(
    title="AI-SOC Threat Pipeline API",
    description="Intelligent API for automated log triage and threat correlation.",
    version="1.0.0"
)

parser = LogParser()
classifier = ThreatClassifier()

@app.post("/analyze", response_model=AnalysisReport)
def analyze_logs(batch: LogBatch):
    """
    Ingest a batch of raw logs, filter anomalies, and classify threats.
    """
    # 1. Parse and filter anomalies
    anomalies = parser.parse(batch.logs)
    
    # 2. Classify and generate alerts
    alerts = classifier.classify_and_score(anomalies)
    
    return AnalysisReport(
        total_logs_analyzed=len(batch.logs),
        threats_detected=len(anomalies),
        alerts=alerts,
        raw_anomalies=anomalies
    )

@app.get("/health")
def health_check():
    return {"status": "healthy"}
