from agents.response_agent import ResponseAgent

agent = ResponseAgent()

result = agent.generate_response("SSH Brute Force")

for action in result:
    print("-", action)
