from typing import List, Literal, Optional, TypedDict


class Message(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


class Conversation(TypedDict):
    messages: Optional[List[Message]]
