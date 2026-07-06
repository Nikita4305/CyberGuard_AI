from agents.log_agent import LogAnalysisAgent

agent = LogAnalysisAgent()

sample = """
Failed password for root from 203.0.113.10 port 22 ssh2
Failed password for root from 203.0.113.10 port 22 ssh2
"""

result = agent.analyze(sample)

print(result)
