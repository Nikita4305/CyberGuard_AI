"""
Threat Intelligence Agent
Assigns severity and threat descriptions.
"""


class ThreatIntelligenceAgent:

    def analyze(self, attack_type):

        threats = {

            "SSH Brute Force": {
                "severity": "HIGH",
                "description": "Multiple failed SSH login attempts detected."
            },

            "Phishing": {
                "severity": "HIGH",
                "description": "Potential credential harvesting attack."
            },

            "Port Scan": {
                "severity": "MEDIUM",
                "description": "Reconnaissance activity detected."
            },

            "Malware": {
                "severity": "CRITICAL",
                "description": "Known malicious file signature."
            },

            "DDoS": {
                "severity": "CRITICAL",
                "description": "Distributed denial of service activity."
            },

            "Ransomware": {
                "severity": "CRITICAL",
                "description": "Mass file encryption behavior detected."
            }
        }

        return threats.get(
            attack_type,
            {
                "severity": "UNKNOWN",
                "description": "No threat intelligence available."
            }
        )
