from typing import List
from urllib.parse import unquote

class LogParser:
    def __init__(self):
        # Basic heuristic rules
        self.suspicious_keywords = [
            "401", "OR 1=1", "UNION", "SELECT", "DROP", "script", "exec"
        ]

    def parse(self, logs: List[str]) -> List[str]:
        """
        Ingest raw logs and filter out normal traffic, isolating threats.
        """
        flagged = []
        for line in logs:
            decoded_line = unquote(line)
            if any(keyword in decoded_line for keyword in self.suspicious_keywords):
                flagged.append(line)
        return flagged
