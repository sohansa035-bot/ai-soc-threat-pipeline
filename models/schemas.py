from pydantic import BaseModel
from typing import List, Optional

class LogEntry(BaseModel):
    raw_log: str

class LogBatch(BaseModel):
    logs: List[str]

class Alert(BaseModel):
    severity: str
    attack_type: str
    confidence: int
    recommended_action: str
    technical_indicators: List[str]

class AnalysisReport(BaseModel):
    total_logs_analyzed: int
    threats_detected: int
    alerts: List[Alert]
    raw_anomalies: List[str]
