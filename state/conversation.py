"""
In-memory conversation history store.
Keyed by (user_id, thread_ts) so each Slack thread maintains its own context.
"""
from collections import defaultdict
from typing import Any

import config

_store: dict[tuple, list[dict[str, Any]]] = defaultdict(list)


def get_history(user_id: str, thread_ts: str) -> list[dict]:
    return list(_store[(user_id, thread_ts)])


def append_message(user_id: str, thread_ts: str, message: dict) -> None:
    key = (user_id, thread_ts)
    _store[key].append(message)
    # Keep only the last N turns to avoid unbounded growth
    max_msgs = config.MAX_HISTORY_TURNS * 2
    if len(_store[key]) > max_msgs:
        _store[key] = _store[key][-max_msgs:]


def clear_history(user_id: str, thread_ts: str) -> None:
    _store.pop((user_id, thread_ts), None)
