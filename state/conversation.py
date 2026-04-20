"""
Manages each user's conversation history, isolating context by using (user_id, thread_ts) as the key.
"""


from collections import defaultdict 
from config import MAX_HISTORY_TURNS

class Conversation:
    def __init__(self):
        self.conversations = defaultdict(list)
        self.max_history_turns = MAX_HISTORY_TURNS * 2
        
    def get_conversation(self, user_id: str, thread_ts: str) -> list[dict]:
        """Get the conversation history for a given user and thread."""
        return self.conversations[(user_id, thread_ts)][:]

    def append(self, user_id: str, thread_ts: str, message: dict):
        """Append a message to the conversation history."""
        self.conversations[(user_id, thread_ts)].append(message)
        if len(self.conversations[(user_id, thread_ts)]) > self.max_history_turns:
            self.conversations[(user_id, thread_ts)] = self.conversations[(user_id, thread_ts)][-self.max_history_turns:]
              
    def clear(self, user_id: str, thread_ts: str):
        """Clear the conversation history for a given user and thread."""
        self.conversations[(user_id, thread_ts)] = []