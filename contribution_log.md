# AI Contribution Log

## 1. Tools Used
- ChatGPT & Gemini for drafting initial script logic and fixing environment variable handling.
- Git Bash & VS Code for environment setup and local code testing.

## 2. AI-Generated Code
- The initial framework and boilerplate structure for `agent.py` utilizing the `google-genai` client configuration.
- Suggestions on how to securely load configurations using `python-dotenv` and environment variables (`os.environ`).

## 3. My Own Contribution
- Reviewed and approved all AI-generated code snippets to ensure correctness.
- Removed hardcoded API keys from the codebase and set up local `.env` security isolation with `.gitignore`.
- Tested the agent locally inside Git Bash and managed the Git repository history resets and force pushes to purge leaked secrets.
- Revoked the compromised API key and generated a secure replacement via Google AI Studio.

## 4. Issues Found in AI Code & Fixes
- **Security Risk:** The initial AI suggestion included hardcoded API keys directly inside the source code file. 
- **Fix:** Manually removed the hardcoded key, refactored the code to check `os.environ.get("GEMINI_API_KEY")`, and implemented a local `.env` workflow to keep credentials secure.
