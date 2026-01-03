class TechnicalGovernanceAgent:
    """
    Silent governance, compliance & security agent.
    NEVER talks to the user.
    """

    def analyze(self, user_message: str) -> dict:
        msg = user_message.lower()

        result = {
            "action": "allow",
            "reason": "No violations"
        }

        jailbreak_patterns = [
            "ignore previous instructions",
            "system prompt",
            "developer message",
            "bypass",
            "override"
        ]

        if any(p in msg for p in jailbreak_patterns):
            return {
                "action": "restrict",
                "reason": "Prompt injection attempt"
            }

        abuse_patterns = [
            "idiot",
            "stupid",
            "i will sue",
            "do it now"
        ]

        if any(p in msg for p in abuse_patterns):
            return {
                "action": "terminate",
                "reason": "Abusive language"
            }

        refund_pressure = [
            "refund now",
            "immediately refund",
            "or else"
        ]

        if any(p in msg for p in refund_pressure):
            return {
                "action": "allow_with_caution",
                "reason": "High-pressure refund attempt"
            }

        return result
