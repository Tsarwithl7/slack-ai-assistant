import os
from dotenv import load_dotenv

load_dotenv()

def _require(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return val

SLACK_BOT_TOKEN    = _require("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN    = _require("SLACK_APP_TOKEN")
ANTHROPIC_API_KEY  = _require("ANTHROPIC_API_KEY")

GOOGLE_TOKEN_PATH  = os.getenv("GOOGLE_TOKEN_PATH", "token.pickle")
GOOGLE_CREDS_PATH  = os.getenv("GOOGLE_CREDS_PATH", "credentials.json")
GOOGLE_CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")

CLAUDE_MODEL       = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")
MAX_HISTORY_TURNS  = int(os.getenv("MAX_HISTORY_TURNS", "20"))
