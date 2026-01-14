"""
main.py
FastAPI app for Design-Flavoured Problems
GET & POST endpoints for all problems
"""

from fastapi import FastAPI
from logic import *
from models import *

app = FastAPI(title="Design Flavoured Problems API")

@app.get("/")
def root():
    return {"message": "Welcome to Design Flavoured Problems API!"}


# 1️⃣ Word Break
@app.post("/word_break")
def api_word_break_post(input: WordBreakInput):
    return {"result": word_break(input.s, input.wordDict)}

@app.get("/word_break")
def api_word_break_get(s: str, wordDict: str):
    word_list = wordDict.split(",")
    return {"result": word_break(s, word_list)}


# 2️⃣ Evaluate Reverse Polish Notation
@app.post("/eval_rpn")
def api_rpn_post(input: RPNInput):
    return {"result": eval_rpn(input.tokens)}

@app.get("/eval_rpn")
def api_rpn_get(tokens: str):
    tokens_list = tokens.split(",")
    return {"result": eval_rpn(tokens_list)}


# 3️⃣ Sliding Window Maximum
@app.post("/sliding_window_max")
def api_sliding_window_post(input: SlidingWindowInput):
    return {"result": max_sliding_window(input.nums, input.k)}

@app.get("/sliding_window_max")
def api_sliding_window_get(nums: str, k: int):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": max_sliding_window(nums_list, k)}


# 4️⃣ Next Greater Element II
@app.post("/next_greater_element")
def api_next_greater_post(input: NextGreaterInput):
    return {"result": next_greater_elements(input.nums)}

@app.get("/next_greater_element")
def api_next_greater_get(nums: str):
    nums_list = [int(x) for x in nums.split(",")]
    return {"result": next_greater_elements(nums_list)}


# 5️⃣ Daily Temperatures
@app.post("/daily_temperatures")
def api_daily_temperatures_post(input: DailyTempsInput):
    return {"result": daily_temperatures(input.temperatures)}

@app.get("/daily_temperatures")
def api_daily_temperatures_get(temperatures: str):
    temps_list = [int(x) for x in temperatures.split(",")]
    return {"result": daily_temperatures(temps_list)}


# 6️⃣ K Closest Points to Origin
@app.post("/k_closest_points")
def api_k_closest_post(input: KClosestInput):
    return {"result": k_closest(input.points, input.k)}

@app.get("/k_closest_points")
def api_k_closest_get(points: str, k: int):
    points_list = [ [int(p.split(":")[0]), int(p.split(":")[1])] for p in points.split(",") ]
    return {"result": k_closest(points_list, k)}


# 7️⃣ Time-Based Key-Value Store
time_map = TimeMap()

@app.post("/timemap_set")
def api_timemap_set_post(input: TimeMapSetInput):
    time_map.set(input.key, input.value, input.timestamp)
    return {"message": "Set successfully"}

@app.post("/timemap_get")
def api_timemap_get_post(input: TimeMapGetInput):
    return {"result": time_map.get(input.key, input.timestamp)}