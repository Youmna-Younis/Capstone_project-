
from openai import OpenAI
import os
import json
import re

from utils.evaluation_state import EvaluationState  # ✅ import here

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def evaluate_responses(state):
    responses = state["responses"]
    eval_state = state.get("evaluation_state", EvaluationState())

    prompt = f"""
            You are evaluating a candidate's performance in a technical interview.
            
            {eval_state.summary()}
            
            Here are the latest responses:
            {json.dumps(responses, indent=2)}
            
            Give cumulative feedback based on the overall trend and detail.
            Respond in JSON format:
            {{
              "score": float (0.0 to 1.0),
              "feedback": string
            }}
            """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    content = response.choices[0].message.content
    json_block = re.search(r"\{.*\}", content, re.DOTALL)
    parsed = json.loads(json_block.group())

    score = parsed["score"]
    feedback = parsed["feedback"]

    eval_state.update(feedback, score)

    return {
        "evaluation": {
            "summary": feedback,
            "score": score,
            "responses": responses,
            "overall_impression": eval_state.overall_impression
        },
        "evaluation_state": eval_state
    }
