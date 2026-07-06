"""
Report Generation Agent
Creates cybersecurity incident reports.
"""


class ReportAgent:

    def generate_report(
        self,
        attack_type,
        confidence,
        severity,
        risk_score,
        priority,
        recommendations
    ):

        report = f"""
==============================
CYBERGUARD AI INCIDENT REPORT
==============================

Attack Type:
{attack_type}

Confidence:
{confidence}%

Severity:
{severity}

Risk Score:
{risk_score}

Priority:
{priority}

Recommended Actions:
"""

        for item in recommendations:
            report += f"\n- {item}"

        report += "\n\nStatus: Incident analyzed successfully."

        return report
