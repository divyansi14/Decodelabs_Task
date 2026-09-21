## Week 1 — Rule-Based Chatbot
**File:** `chatbot.py`

### Objective
Build a terminal-based chatbot that responds to user input using
rule-based pattern matching — no ML involved, focused on clean intent
handling and lookup logic.

### Approach
- Dictionary + `.get()` lookup for intent matching (not if-elif chains)
- Input sanitized with `.lower().strip()` before matching
- Extended beyond the base brief with a multi-layer lookup system,
  additional intents, and a named bot personality ("Byte")


### How to Run
```
python chatbot.py
```

---

## Week 2 — Iris Species Classifier (KNN)
**File:** `iris_classifier.py` 

### Objective
Build a supervised ML classifier to predict Iris flower species from
measurement data, covering the complete ML workflow end-to-end.

### Approach
- **Model:** K-Nearest Neighbors (KNN) via scikit-learn
- **Pipeline:** load data → feature scaling → train/test split → train
  → evaluate
- Evaluation went beyond raw accuracy — precision, recall, F1 score, and
  a confusion matrix were used, since accuracy alone can be misleading
  (especially on imbalanced datasets)

### Tech Stack
Python, scikit-learn, pandas

### How to Run
```
python iris_classifier.py
```

---

## Week 3 — Tech Stack Recommender
**Files:** `recommender.py`, `raw_skills.csv`

### Objective
Build a content-based recommendation engine that maps a user's stated
skills to the most relevant career paths, using similarity logic.

### Approach
- **Method:** Content-based filtering (chosen over collaborative
  filtering — no historical user data required, and it sidesteps the
  "cold start" problem)
- **Vectorization:** TF-IDF (`TfidfVectorizer`) — weights each skill by
  how distinctive it is across roles, rather than treating all skills
  equally
- **Matching:** Cosine Similarity — measures the angle between the
  user's skill vector and each role's vector, so it isn't skewed by how
  many skills a role happens to list
- **Pipeline:** Ingestion (load 20 roles + capture ≥3 user skills) →
  Scoring (TF-IDF + cosine similarity) → Sorting (rank descending) →
  Filtering (Top-3 output)
- Handles the edge case where none of the user's skills match anything
  in the vocabulary, instead of showing a misleading result

### Tech Stack
Python, pandas, scikit-learn (`TfidfVectorizer`, `cosine_similarity`)

### How to Run
```
python recommender.py
```

### Sample Output
```
Tech Stack Recommender ready — 20 career paths loaded.

Enter your skills one at a time (minimum 3).
Type 'done' when finished.

Skill 1: Python
Skill 2: Docker
Skill 3: Kubernetes
Skill 4: done

TOP 3 RECOMMENDED CAREER PATHS
1. Site Reliability Engineer — 38.4% match
2. Cloud Architect — 38.2% match
3. DevOps Engineer — 36.1% match
```

---


- Python, VS Code (PowerShell terminal)
- Project directory: `D:\DecodeLabs_Internship\`
