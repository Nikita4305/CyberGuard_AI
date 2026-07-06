"""
Coordinator Agent
Coordinates all CyberGuard AI agents.
"""

from agents.log_agent import LogAnalysisAgent
from agents.threat_agent import ThreatIntelligenceAgent
from agents.risk_agent import RiskAssessmentAgent
from agents.response_agent import ResponseAgent
from agents.report_agent import ReportAgent


class CoordinatorAgent:

    def __init__(self):
        self.log_agent = LogAnalysisAgent()
        self.threat_agent = ThreatIntelligenceAgent()
        self.risk_agent = RiskAssessmentAgent()
        self.response_agent = ResponseAgent()
        self.report_agent = ReportAgent()

    def analyze_incident(self, incident):

        # Step 1
        attack = self.log_agent.analyze(incident)

        # Step 2
        threat = self.threat_agent.analyze(
            attack["attack_type"]
        )

        # Step 3
        risk = self.risk_agent.assess(
            threat["severity"]
        )

        # Step 4
        response = self.response_agent.generate_response(
            attack["attack_type"]
        )

        # Step 5
        report = self.report_agent.generate_report(
            attack_type=attack["attack_type"],
            confidence=attack["confidence"],
            severity=threat["severity"],
            risk_score=risk["risk_score"],
            priority=risk["priority"],
            recommendations=response
        )

        return report
