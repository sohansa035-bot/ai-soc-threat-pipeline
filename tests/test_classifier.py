import pytest
from classifier.engine import ThreatClassifier

def test_classifier_empty_anomalies():
    classifier = ThreatClassifier()
    alerts = classifier.classify_and_score([])
    assert len(alerts) == 0

def test_classifier_brute_force():
    classifier = ThreatClassifier()
    anomalies = [
        '192.168.1.45 - - [30/May/2026:23:01:12] "POST /login HTTP/1.1" 401 230'
    ]
    alerts = classifier.classify_and_score(anomalies)
    assert len(alerts) == 1
    assert alerts[0].attack_type == "Brute Force"
    assert alerts[0].severity == "High"

def test_classifier_sqli():
    classifier = ThreatClassifier()
    anomalies = [
        '192.168.1.102 - - [30/May/2026:23:02:45] "GET /search?id=1%20OR%201=1 HTTP/1.1" 500 1240'
    ]
    alerts = classifier.classify_and_score(anomalies)
    assert len(alerts) == 1
    assert alerts[0].attack_type == "SQL Injection"
    assert alerts[0].severity == "Critical"
