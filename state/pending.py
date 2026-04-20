"""
In-memory store for operations awaiting user confirmation.
Each pending op is keyed by a unique action_id embedded in the Block Kit button.
"""
import uuid
from dataclasses import dataclass
from typing import Any

@dataclass
class PendingOperation:
    tool_name: str
    tool_input: dict[str, Any]
    tool_use_id: str      # Claude's tool_use block id — needed for tool_result
    user_id: str
    channel_id: str
    thread_ts: str
    message_ts: str       # ts of the placeholder message to update


_store: dict[str, PendingOperation] = {}


def create_pending(op: PendingOperation) -> str:
    """Store a pending operation and return its unique action_id."""
    action_id = str(uuid.uuid4())
    _store[action_id] = op
    return action_id


def consume_pending(action_id: str) -> PendingOperation | None:
    """Remove and return a pending operation (or None if already handled)."""
    return _store.pop(action_id, None)
