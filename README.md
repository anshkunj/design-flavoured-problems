# 🚀 Design-Flavored Problems

A collection of **design-inspired algorithm problems** simulating real-world system scenarios. Focused on queues, stacks, scheduling, and optimization challenges, each problem is explained with diagrams, patterns, and efficient solutions.

---

## 🧠 Features
- Python solutions mimicking real system designs  
- Optimized algorithms with clean logic  
- Diagrams and explanations for practical understanding  
- JSON-friendly examples where applicable  
- Focus on abstraction and problem decomposition  

---

## 📂 Repo Structure

design-flavored-problems/  
├── README.md                   # This file  
├── queue_task_scheduler.py     # Task scheduling patterns  
├── stack_min_tracker.py        # Stack design with auxiliary operations  
├── sliding_window_max_design.py # Real-world windowed system  
├── lru_cache_simulation.py      # LRU cache design problem  
├── recent_counter.py           # Rolling counter simulation  
└── ... (add more design-focused problems)  

---

## 🏗️ How This Repo Works
- Each `.py` file contains a single problem solution  
- Core design logic is explained with **diagrams + comments**  
- Patterns highlighted for **backend, system design, and algorithmic thinking**  
- Optimized solutions for efficiency and scalability  

---

## 📌 Problem Patterns Covered
- Queue and stack simulations  
- Scheduling and rolling counters  
- Cache and sliding window system designs  
- Maximum / minimum tracking in streams  
- Real-world abstractions mapped to algorithms  

---

## ⚙️ Installation & Run

1) Clone the repository  
git clone https://github.com/anshkunj/design-flavoured-problems.git  
cd design-flavoured-problems  

2) Install dependencies  
pip install -r requirements.txt  

3) Run the server  
uvicorn main:app --reload  

---

## 🌐 API Documentation

Swagger UI: http://127.0.0.1:8000/docs  

ReDoc: http://127.0.0.1:8000/redoc  

---

## 🌐 Live API

Base URL:  
https://design-flavoured-problems.onrender.com  
Docs:  
https://design-flavoured-problems.onrender.com/docs 

---

## 🧪 Example (LRU Cache Simulation)

```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)      # evicts key 2
print(cache.get(2))  # returns -1
```

- Simulates a real LRU cache  
- Handles get/put operations in O(1)  
- Demonstrates abstraction and system design thinking  

---

## 🚧 Edge Cases Handled
- Empty inputs  
- Large number of operations  
- Boundary conditions for queues, stacks, and caches  
- Optimized for performance  

---

## 🛠️ Tech Stack
- Python 3.x  
- Standard libraries (`collections`, `heapq`, `itertools`)  
- Optional: Jupyter Notebook for visualization  

---

## 📄 Licence
MIT Licence  

---

## 👤 Author
**anshkunj**  
GitHub: https://github.com/anshkunj  
Fiverr: https://www.fiverr.com/s/xX9mNXB  

---

## ⭐ Support
If you find this repo helpful, give it a star ⭐  
It motivates me to create more real-world algorithm & system design projects 🚀  

---

## 🔹 Note
This repo is regularly updated with new design-flavored problems and explanations.