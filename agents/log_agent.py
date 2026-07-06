"""
Log Analysis Agent
Detects cyber attack patterns.
"""


class LogAnalysisAgent:

    def analyze(self, incident):

        incident = incident.lower()

        # SSH brute force
        if "failed password" in incident or "ssh2" in incident:
            return {
                "attack_type": "SSH Brute Force",
                "confidence": 95
            }

        # phishing
        elif "paypal" in incident or "login" in incident:
            return {
                "attack_type": "Phishing",
                "confidence": 90
            }

        # port scan
        elif "port scan" in incident or "scanned ports" in incident:
            return {
                "attack_type": "Port Scan",
                "confidence": 85
            }

        # malware hash
        elif len(incident.strip()) == 32:
            return {
                "attack_type": "Malware",
                "confidence": 90
            }

        # ddos
        elif "requests per minute" in incident:
            return {
                "attack_type": "DDoS",
                "confidence": 95
            }

        # ransomware
        elif "encrypted" in incident:
            return {
                "attack_type": "Ransomware",
                "confidence": 98
            }

        return {
            "attack_type": "Unknown",
            "confidence": 0
        }
