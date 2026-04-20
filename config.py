"""集中管理所有环境变量，启动时快速验证必填项。"""

import os
from dotenv import load_dotenv

load_dotenv()


def _require(key: str) -> str:
    """Read a required environment variable. Raises EnvironmentError if missing."""
    value = os.getenv(key)
    if not value:
        raise EnvironmentError(
            f"Missing required environment variable: '{key}'. Check your .env file."
        )
    return value


# ── 必填 ──────────────────────────────────────
SLACK_BOT_TOKEN: str   = _require("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN: str   = _require("SLACK_APP_TOKEN")
ANTHROPIC_API_KEY: str = _require("ANTHROPIC_API_KEY")

# ── 选填（含默认值）───────────────────────────
GOOGLE_TOKEN_PATH: str  = os.getenv("GOOGLE_TOKEN_PATH", "token.pickle")
GOOGLE_CREDS_PATH: str  = os.getenv("GOOGLE_CREDS_PATH", "credentials.json")
GOOGLE_CALENDAR_ID: str = os.getenv("GOOGLE_CALENDAR_ID", "primary")
CLAUDE_MODEL: str       = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")
MAX_HISTORY_TURNS: int  = int(os.getenv("MAX_HISTORY_TURNS", "20"))
