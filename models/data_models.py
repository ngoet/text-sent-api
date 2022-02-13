from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEnum(str, Enum):
    success = "success"
    unsuccessful = "unsuccessful"


class Response(BaseModel):
    status: Optional[StatusEnum] = None
    sentiment_score: Optional[float] = None
    error: Optional[str] = None
    warning: Optional[str] = None


class Payload(BaseModel):
    text: str
