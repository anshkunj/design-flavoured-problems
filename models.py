"""
models.py
Pydantic models for Design-Flavoured Problems API
"""

from pydantic import BaseModel
from typing import List

# Word Break
class WordBreakInput(BaseModel):
    s: str
    wordDict: List[str]

# RPN
class RPNInput(BaseModel):
    tokens: List[str]

# Sliding Window Maximum
class SlidingWindowInput(BaseModel):
    nums: List[int]
    k: int

# Next Greater Element II
class NextGreaterInput(BaseModel):
    nums: List[int]

# Daily Temperatures
class DailyTempsInput(BaseModel):
    temperatures: List[int]

# K Closest Points
class KClosestInput(BaseModel):
    points: List[List[int]]
    k: int

# Time-based KV
class TimeMapSetInput(BaseModel):
    key: str
    value: str
    timestamp: int

class TimeMapGetInput(BaseModel):
    key: str
    timestamp: int