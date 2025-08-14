from dataclasses import dataclass
from typing import Optional

@dataclass
class TweetResponse:
    success: bool
    url: str = ""
    error: str = ""
    status_code: int = 0

@dataclass
class UserResponse:
    success: bool
    user_data: Optional[dict] = None
    error: str = ""
    status_code: int = 0