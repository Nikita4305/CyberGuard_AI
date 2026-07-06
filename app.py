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

analyze = st.button(
    "🚨 Analyze Incident",
    use_container_width=True
)

if analyze:

    if incident.strip():

        with st.spinner(
            "CyberGuard AI analyzing..."
        ):

            report = coordinator.analyze_incident(
                incident
            )

            ai_analysis = gemini.analyze(
                incident
            )

        st.success(
            "Analysis completed"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.subheader(
                "📋 Multi-Agent Analysis"
            )
            st.code(
                report,
                language=None
            )

        with col2:
            st.subheader(
                "🤖 Gemini Security Analyst"
            )
            st.write(
                ai_analysis
            )

    else:
        st.error(
            "Please enter a security incident."
        )
