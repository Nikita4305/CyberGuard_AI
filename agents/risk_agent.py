"""
Risk Assessment Agent
Calculates risk score and priority.
"""


class RiskAssessmentAgent:

    def assess(self, severity):

        risk_map = {

            "LOW": {
                "risk_score": 25,
                "priority": "P4"
            },

            "MEDIUM": {
                "risk_score": 50,
                "priority": "P3"
            },

            "HIGH": {
                "risk_score": 85,
                "priority": "P2"
            },

            "CRITICAL": {
                "risk_score": 100,
                "priority": "P1"
            }
        }

        return risk_map.get(
            severity,
            {
                "risk_score": 0,
                "priority": "UNKNOWN"
            }
        )
