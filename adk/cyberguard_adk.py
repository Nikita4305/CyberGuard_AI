from google.adk.agents import Agent

from agents.log_agent import LogAnalysisAgent
from agents.threat_agent import ThreatIntelligenceAgent
from agents.risk_agent import RiskAssessmentAgent


# Existing CyberGuard agents
log_agent = LogAnalysisAgent()
threat_agent = ThreatIntelligenceAgent()
risk_agent = RiskAssessmentAgent()


def analyze_incident(incident: str):

    # Log analysis
    attack = log_agent.analyze(
        incident
    )

    # Threat classification
    threat = threat_agent.analyze(
        attack["attack_type"]
    )

    # Risk scoring
    risk = risk_agent.assess(
        threat["severity"]
    )

    return {
        "attack": attack,
        "threat": threat,
        "risk": risk
    }


# Google ADK Agent
cyberguard_agent = Agent(
    name="CyberGuardCoordinator",

    model="gemini-2.5-flash",

    description="""
    Multi-agent cybersecurity
    incident response coordinator.
    """,

    instruction="""
    Analyze cybersecurity incidents
    using multiple security agents.
    """,

    tools=[
        analyze_incident
    ],
)