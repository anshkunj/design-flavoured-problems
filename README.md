<p align="center">
  <img src="https://github.com/anshkunj/design-flavoured-problems/blob/1e809df95b193b2c65e4bc899854d1df15d844b8/file_0000000033087207b98238d19c87fd41.png" alt="Design Flavoured Problems" width="1200">
</p>

<h1 align="center">Design Flavoured Problems</h1>
<p align="center">Coding Challenges with a Creative Twist 🚀</p>

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
```
design-flavored-problems/  
├── main.py          # FastAPI app & routes
├── logic.py         # Core algorithm implementations  
├── models.py        # Pydantic request models  
├── .gitignore  
├── requirements.txt  
├── render.yaml  
├── README.md       # Project Overview  
└── LICENSE         # Licence file (MIT)  
```
---

## 🏗️ How This Repo Works  
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

Base URL: https://design-flavoured-problems.onrender.com  
Docs: https://design-flavoured-problems.onrender.com/docs 

---

## 🔗 Endpoints – Design-Flavoured Problems

This section documents conceptual API-style endpoints mapped to the functions in logic.py.  
Each endpoint shows example input and expected output.

### 1️⃣ Word Break
**Endpoint:** /design/word-break

Input:
s = "leetcode"
wordDict = ["leet","code"]

Output:
result = true

### 2️⃣ Evaluate Reverse Polish Notation
**Endpoint:** /design/eval-rpn

Input:
tokens = ["2","1","+","3","*"]

Output:
result = 9

### 3️⃣ Sliding Window Maximum
**Endpoint:** /design/sliding-window-maximum

Input:
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Output:
result = [3,3,5,5,6,7]

### 4️⃣ Next Greater Element II
**Endpoint:** /design/next-greater-element-ii

Input:
nums = [1,2,1]

Output:
result = [2,-1,2]

### 5️⃣ Daily Temperatures
**Endpoint:** /design/daily-temperatures

Input:
T = [73,74,75,71,69,72,76,73]

Output:
result = [1,1,4,2,1,1,0,0]

### 6️⃣ K Closest Points to Origin
**Endpoint:** /design/k-closest-points

Input:
points = [[1,3],[-2,2]]
k = 1

Output:
result = [[-2,2]]

### 7️⃣ Time-Based Key-Value Store

#### Set
**Endpoint:** /design/timemap/set

Input:
key = "foo"
value = "bar"
timestamp = 1

Output:
ack = true

#### Get
**Endpoint:** /design/timemap/get

Input:
key = "foo"
timestamp = 1

Output:
result = "bar"

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

## 🤝 Contributing
Contributors are welcome!  
• Add new sliding window problems  
• Improve explanations  
• Optimise exists code  

---

## 👤 Author
**anshkunj**  
### 📫 Let’s connect
- **GitHub:** https://github.com/anshkunj
- **LinkedIn:** https://linkedin.com/in/anshkunj
- **Portfolio:** https://anshkunj.github.io/Portfolio
- **LeetCode:** https://leetcode.com/u/anshkunj
- **Devpost:** https://devpost.com/anshkunj
- **HackerRank:** https://www.hackerrank.com/profile/anshkunj
- **AtCoder:** https://atcoder.jp/users/anshkunj
- **Codeforces:** https://codeforces.com/profile/anshkunj
- **Fiverr:** https://www.fiverr.com/anshkunj
- **Freelancer:** https://www.freelancer.com/u/anshkunj

---

## ⭐ Support
If you find this repo helpful, give it a star ⭐  
It motivates me to create more real-world algorithm & system design projects 🚀  

---

## 🔹 Note
This repo is regularly updated with new design-flavored problems and explanations.
