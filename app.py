import streamlit as st

from agents.coordinator import CoordinatorAgent
from agents.gemini_agent import GeminiSecurityAgent


coordinator = CoordinatorAgent()
gemini = GeminiSecurityAgent()


st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)


st.title("🛡️ CyberGuard AI")
st.caption(
    "Multi-Agent Cybersecurity Incident Response Assistant"
)

st.divider()


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


if st.button(
    "🚨 Analyze Incident",
    use_container_width=True
):

    if incident.strip():

        with st.spinner(
            "CyberGuard AI analyzing..."
        ):

            ai_analysis = gemini.analyze(
                incident
            )

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

        st.success(
            "Analysis completed"
        )

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
                threat["severity"]
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

        st.divider()

        st.subheader(
            "🛠 Recommended Actions"
        )

        for action in actions:
            st.success(action)

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
