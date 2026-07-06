from agents.report_agent import ReportAgent

agent = ReportAgent()

report = agent.generate_report(
    attack_type="SSH Brute Force",
    confidence=95,
    severity="HIGH",
    risk_score=85,
    priority="P2",
    recommendations=[
        "Block the source IP address",
        "Enable multi-factor authentication",
        "Reset compromised credentials"
    ]
)

print(report)
