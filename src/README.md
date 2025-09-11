# IAM Role Analyzer

**IAM Role Analyzer** is a Python CLI tool that helps cloud security engineers assess the security of AWS IAM roles. It automatically fetches all inline and managed policies attached to a role, analyzes them using AI, and provides risk scores along with actionable least-privilege recommendations.

---

## Features

- Fetches **inline** and **managed IAM policies** for a given role.  
- Uses **Claude AI** to analyze policies for:
  - Overly permissive actions  
  - Wildcard resources (`*`)  
  - Privilege escalation risks  
- Returns a **risk score** (0–100) per policy and overall role.  
- Provides **actionable recommendations** for least-privilege access.  
- CLI interface with **Rich** for colored output.  
- Handles errors gracefully and provides fallback results.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/iam-role-analyzer.git
cd iam-role-analyzer
