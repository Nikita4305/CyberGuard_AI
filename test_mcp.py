from mcp.threat_server import ThreatMCPServer

server = ThreatMCPServer()

print(
    server.lookup(
        "203.0.113.10"
    )
)
