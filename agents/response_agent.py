"""
Response Agent
Generates incident response recommendations.
"""


class ResponseAgent:

    def generate_response(self, attack_type):

        responses = {

            "SSH Brute Force": [
                "Block the source IP address",
                "Enable multi-factor authentication",
                "Reset compromised credentials",
                "Review authentication logs"
            ],

            "Phishing": [
                "Block the malicious domain",
                "Reset affected user credentials",
                "Notify impacted users",
                "Perform phishing awareness training"
            ],

            "Port Scan": [
                "Block suspicious IP addresses",
                "Review firewall rules",
                "Monitor network activity",
                "Harden exposed services"
            ],

            "Malware": [
                "Isolate the affected system",
                "Run malware analysis",
                "Remove malicious files",
                "Perform a full system scan"
            ],

            "DDoS": [
                "Enable rate limiting",
                "Block attacking IP addresses",
                "Use DDoS mitigation services",
                "Scale infrastructure resources"
            ],

            "Ransomware": [
                "Disconnect affected hosts",
                "Restore from backups",
                "Preserve forensic evidence",
                "Notify the incident response team"
            ]
        }

        return responses.get(
            attack_type,
            ["No response recommendations available."]
        )
