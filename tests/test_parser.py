import pytest
from parser.log_parser import LogParser

def test_log_parser_clean_traffic():
    parser = LogParser()
    logs = [
        '192.168.1.20 - - [30/May/2026:23:01:00] "GET /index.html HTTP/1.1" 200 4325',
        '192.168.1.25 - - [30/May/2026:23:03:00] "GET /images/logo.png HTTP/1.1" 200 12040'
    ]
    anomalies = parser.parse(logs)
    assert len(anomalies) == 0

def test_log_parser_detects_sqli():
    parser = LogParser()
    logs = [
        '192.168.1.102 - - [30/May/2026:23:02:45] "GET /search?id=1%20OR%201=1 HTTP/1.1" 500 1240'
    ]
    anomalies = parser.parse(logs)
    assert len(anomalies) == 1
    assert "%20OR%201=1" in anomalies[0]
