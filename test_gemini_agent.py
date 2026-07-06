from agents.gemini_agent import GeminiSecurityAgent

agent = GeminiSecurityAgent()

incident = """
Failed password for root from 203.0.113.10 port 22 ssh2
Failed password for root from 203.0.113.10 port 22 ssh2
Failed password for root from 203.0.113.10 port 22 ssh2
"""

result = agent.analyze(
    incident
)

print(result)
