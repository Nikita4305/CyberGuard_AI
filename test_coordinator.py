from agents.coordinator import CoordinatorAgent

coordinator = CoordinatorAgent()

incident = """
Failed password for root from 203.0.113.10 port 22 ssh2
Failed password for root from 203.0.113.10 port 22 ssh2
Failed password for root from 203.0.113.10 port 22 ssh2
"""

result = coordinator.analyze_incident(incident)

print(result)
