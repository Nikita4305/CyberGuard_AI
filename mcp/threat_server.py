"""
CyberGuard AI MCP Threat Server
"""

THREAT_DATABASE = {

    "203.0.113.10": {
        "reputation": "Malicious",
        "confidence": 95,
        "category": "Brute Force Source"
    },

    "44d88612fea8a8f36de82e1278abb02f": {
        "reputation": "Malware",
        "confidence": 99,
        "category": "Trojan"
    },

    "paypal-security-verification-login.com": {
        "reputation": "Phishing",
        "confidence": 90,
        "category": "Credential Theft"
    }
}


class ThreatMCPServer:

    def lookup(self, indicator):

        return THREAT_DATABASE.get(
            indicator,
            {
                "reputation": "Unknown",
                "confidence": 0,
                "category": "Unknown"
            }
        )
