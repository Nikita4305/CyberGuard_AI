import streamlit as st

from agents.coordinator import CoordinatorAgent


coordinator = CoordinatorAgent()


st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberGuard AI")

st.subheader(
    "Multi-Agent Cybersecurity Incident Response Assistant"
)

st.markdown("---")

incident = st.text_area(
    "Paste Security Incident",
    height=200,
    placeholder="""
Examples:

Failed password for root from 203.0.113.10 port 22 ssh2

paypal-security-verification-login.com

Port scan detected from 192.168.1.55

44d88612fea8a8f36de82e1278abb02f

50000 requests per minute from multiple IP addresses

200 files encrypted within 2 minutes
"""
)

if st.button("Analyze Incident"):

    if incident.strip():

        with st.spinner(
            "CyberGuard AI is analyzing..."
        ):

            report = coordinator.analyze_incident(
                incident
            )

        st.success(
            "Analysis completed successfully"
        )

        st.text(report)

    else:

        st.error(
            "Please enter a security incident."
        )
