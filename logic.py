"""
logic.py
Contains all Design-Flavoured Problem solutions
"""

from typing import List
from collections import deque
import heapq

# 1️⃣ Word Break
def word_break(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

# 2️⃣ Evaluate Reverse Polish Notation
def eval_rpn(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a+b)
            elif token == '-':
                stack.append(a-b)
            elif token == '*':
                stack.append(a*b)
            else:
                stack.append(int(a/b))  # truncate toward zero
        else:
            stack.append(int(token))
    return stack[0]

# 3️⃣ Sliding Window Maximum
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    dq = deque()
    result = []
    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# 4️⃣ Next Greater Element II
def next_greater_elements(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2*n):
        num = nums[i % n]
        while stack and nums[stack[-1]] < num:
            res[stack.pop()] = num
        if i < n:
            stack.append(i)
    return res

# 5️⃣ Daily Temperatures
def daily_temperatures(T: List[int]) -> List[int]:
    n = len(T)
    res = [0]*n
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res

# 6️⃣ K Closest Points to Origin
def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = [(x**2 + y**2, [x, y]) for x, y in points]
    heapq.heapify(heap)
    result = [heapq.heappop(heap)[1] for _ in range(k)]
    return result

# 7️⃣ Time-Based Key-Value Store
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        l, r = 0, len(arr)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m+1
            else:
                r = m-1
        return res