import anthropic
import json

claude_api_key = "CLAUDE_API_KEY"  # Replace with your actual Claude API key
client = anthropic.Client(api_key=claude_api_key)

def analyze_policy(policy_name, policy_doc):
    policies_json = json.dumps(policy_doc, indent=2)
    prompt = f"""
You are a cloud security analyst.

Analyze the following AWS IAM policy "{policy_name}":

{policies_json}

- Identify security risks (overly permissive actions, wildcard resources, privilege escalation).
- Assign a risk score from 0 (safe) to 100 (critical).
- Provide actionable least-privilege recommendations.

Return your answer in JSON format:
{{"risk_score": int, "risks": [], "recommendations": []}}
"""

    try:
        response = client.completions.create(
            model="claude-2",
            max_tokens=1000,
            prompt=f"{anthropic.HUMAN_PROMPT}{prompt}{anthropic.AI_PROMPT}"
        )

        result_text = response.completion.strip()
        return json.loads(result_text)

    except Exception as e:
        # Catch parsing errors or API errors
        return {
            "risk_score": 0,
            "risks": [f"Failed to parse AI output: {str(e)}"],
            "recommendations": []
        }
