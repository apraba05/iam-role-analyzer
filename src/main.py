import typer
from aws_cli import get_role_policies
from ai_analyst import analyze_policies
from rich import print

app = typer.Typer()

@app.command()
def scan_role(role_name: str):
    print(f"[bold blue]Scanning IAM Role:[/bold blue] {role_name}")
    policies = get_role_policies(role_name)

    all_scores = []
    all_findings = []
    all_recommendations = []

    for name, doc in policies.items():
        result = analyze_policies(name, doc)
        all_scores.append(result['score'])
        all_findings.extend(result['risks'])
        all_recommendations.extend(result['recommendations'])

    role_score = sum(all_scores) / len(all_scores) if all_scores else 0

    print(f"[bold]Overall Role Security Score:[/bold] {role_score:.2f}/10")
    print("[bold yellow]Risks Found:[/bold yellow]")
    for risk in all_findings:
        print(f"- {risk}")

    print("[bold green]Recommendations:[/bold green]")
    for rec in all_recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    app()