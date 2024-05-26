from dataclasses import dataclass
from typing import List

@dataclass
class Poruka:
    message_text: str
    is_user: bool
    timestamp: str

@dataclass
class ChatSesija:
    id: int
    session_name: str
    messages: List[Poruka]
    created_at: str
