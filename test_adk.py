from adk.cyberguard_adk import analyze_incident


incident = """
Failed password for root
from 203.0.113.10
port 22 ssh2
"""


result = analyze_incident(
    incident
)

print(result)
