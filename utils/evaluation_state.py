class EvaluationState:
    def __init__(self):
        self.past_feedback = []
        self.previous_scores = []
        self.overall_impression = "Neutral"

    def update(self, feedback, score):
        self.past_feedback.append(feedback)
        self.previous_scores.append(score)
        self.overall_impression = self._derive_impression()

    def _derive_impression(self):
        if not self.previous_scores:
            return "Neutral"
        avg = sum(self.previous_scores) / len(self.previous_scores)
        if avg > 0.8:
            return "Strong Candidate"
        elif avg < 0.4:
            return "Weak Candidate"
        return "Moderate Potential"


    def summary(self):
        recent = "\n".join(f"- {fb}" for fb in self.past_feedback[-3:])
        return f"Recent feedback:\n{recent}\nOverall impression: {self.overall_impression}"
