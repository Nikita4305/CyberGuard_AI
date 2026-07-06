import streamlit as st

from agents.coordinator import CoordinatorAgent
from agents.gemini_agent import GeminiSecurityAgent
from mcp.threat_server import ThreatMCPServer


# Initialize components
coordinator = CoordinatorAgent()
gemini = GeminiSecurityAgent()
mcp_server = ThreatMCPServer()


# Page configuration
st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)


# Header
st.title("🛡️ CyberGuard AI")
st.caption(
    "Multi-Agent Cybersecurity Incident Response Assistant"
)

st.divider()


# Input box
incident = st.text_area(
    "Security Incident",
    height=180,
    placeholder="""
Examples:

Failed password for root from 203.0.113.10 port 22 ssh2

paypal-security-verification-login.com

Port scan detected from 192.168.1.55
44d88612fea8a8f36de82e1278abb02f
"""
)


# Analyze button
# Analyze button
if st.button(
    "🚨 Analyze Incident",
    use_container_width=True
):

    if incident.strip():

        # Multi-agent analysis first
        attack = coordinator.log_agent.analyze(
            incident
        )

        threat = coordinator.threat_agent.analyze(
            attack["attack_type"]
        )

        risk = coordinator.risk_agent.assess(
            threat["severity"]
        )

        actions = (
            coordinator.response_agent.generate_response(
                attack["attack_type"]
            )
        )

        # Gemini analysis using the same confidence score
        with st.spinner(
            "CyberGuard AI analyzing..."
        ):

            ai_analysis = gemini.analyze(
                incident,
                confidence=attack["confidence"]
            )

        # Severity badge
        severity = threat["severity"]

        if severity == "LOW":
            severity_display = "🟢 LOW"
        elif severity == "MEDIUM":
            severity_display = "🟡 MEDIUM"
        elif severity == "HIGH":
            severity_display = "🟠 HIGH"
        else:
            severity_display = "🔴 CRITICAL"

        st.success(
            "Analysis completed"
        )

        # Incident Summary
        st.subheader(
            "🚨 Incident Summary"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Attack Type",
                attack["attack_type"]
            )

        with col2:
            st.metric(
                "Severity",
                severity_display
            )

        with col3:
            st.metric(
                "Confidence",
                f"{attack['confidence']}%"
            )

        with col4:
            st.metric(
                "Priority",
                risk["priority"]
            )

        # MCP Threat Intelligence
        st.divider()

        st.subheader(
            "🌐 Threat Intelligence (MCP)"
        )

        indicator = "203.0.113.10"

        intel = mcp_server.lookup(
            indicator
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Reputation",
                intel["reputation"]
            )

        with col2:
            st.metric(
                "Confidence",
                f"{intel['confidence']}%"
            )

        with col3:
            st.metric(
                "Category",
                intel["category"]
            )

        # Attack Timeline
        st.divider()

        st.subheader(
            "🕒 Attack Timeline"
        )

        timeline = [
            "08:21:01 - Failed login detected",
            "08:21:05 - Repeated login attempt",
            "08:21:09 - Attack pattern identified",
            "08:21:14 - Risk analysis completed",
            "08:21:18 - Response generated"
        ]

        for event in timeline:
            st.info(event)

        # Recommended Actions
        st.divider()

        st.subheader(
            "🛠 Recommended Actions"
        )

        for action in actions:
            st.success(action)

        # Gemini Analysis
        st.divider()

        st.subheader(
            "🤖 Gemini Security Analysis"
        )

        st.write(
            ai_analysis
        )

    else:

        st.error(
            "Please enter a security incident."
        )
