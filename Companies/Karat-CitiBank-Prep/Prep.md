# 🎯 Karat Interview Study Plan — Citi AI Engineer
### Interview: Monday, March 23, 2026 @ 10:00 AM CST
### Language: Python | Via: Capgemini → Karat → Citibank

---

## ⏰ Interview Format Recap

| Section | Duration | What to Expect |
|---------|----------|----------------|
| Intro | ~5 min | Brief self-intro |
| Discussion & Analysis | ~10 min | Domain knowledge questions (AI/ML, system design concepts) |
| Live Coding | ~40 min | 1-2 coding problems with multi-part follow-ups |
| Wrap-up | ~5 min | Your questions |

**Key Rule:** You need to solve **at least 2 parts** to pass. Focus on **correctness over optimization**.

---

## 📅 DAY 1 — Friday, March 20 (Today)
### Theme: "Learn the Patterns" (4-5 hours)

### Morning/Afternoon: Core Karat Questions (3 hours)

Solve these in order of priority. These are the **most recycled** Karat problems.

#### ✅ Problem 1: Badge Access (Entry/Exit) — 45 min
> Given an ordered list of employees who badged to enter or exit a room,
> find: (a) employees who entered without exiting, (b) employees who exited without entering.

```
Input:
badge_records = [
  ["Martha", "exit"], ["Paul", "enter"], ["Martha", "enter"],
  ["Steve", "enter"], ["Martha", "exit"], ["Jennifer", "enter"],
  ["Paul", "enter"], ["Curtis", "exit"], ["Curtis", "enter"],
  ["Paul", "exit"], ["Martha", "enter"], ["Martha", "exit"],
  ["Jennifer", "exit"], ["Paul", "enter"], ["Paul", "enter"],
  ["Martha", "exit"],
]
Output: (entered_without_exit, exited_without_enter)
```

**Pattern:** Hash Set tracking state
**Follow-up:** Find employees who badged 3+ times within a 1-hour window (sliding window + hash map)

---

#### ✅ Problem 2: Subdomain Visit Count (LeetCode 811) — 30 min
> Given a list like ["900 google.com", "50 mail.yahoo.com"], aggregate counts across all subdomains.
> e.g., "mail.yahoo.com" also counts toward "yahoo.com" and "com"

**Pattern:** String splitting + Hash Map counting

---

#### ✅ Problem 3: Find Rectangle of 0s in Matrix — 45 min
> Given a matrix of 1s and 0s (with exactly one rectangle of 0s), find the top-left and bottom-right corners.

```
Input:
[
  [1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1],
]
Output: (1, 1), (2, 3)
```

**Pattern:** Matrix traversal
**Follow-up:** Find MULTIPLE rectangles of 0s → use visited set + BFS/DFS

---

#### ✅ Problem 4: Shared Courses (Student Pairs) — 45 min
> Given student-course enrollment pairs, find shared courses for every pair of students.

```
Input:
enrollments = [
  ["Alice", "Python"], ["Bob", "Python"], ["Alice", "Java"],
  ["Bob", "Java"], ["Alice", "ML"], ["Charlie", "Python"],
]
Output:
  ("Alice","Bob"): ["Python","Java"]
  ("Alice","Charlie"): ["Python"]
  ("Bob","Charlie"): ["Python"]
```

**Pattern:** Hash Map (student → set of courses) + Pair generation with set intersection

---

### Evening: Discussion Questions Prep (1-2 hours)

Since this is an **AI Engineer** role, prepare concise answers for:

#### AI/ML Discussion Topics
1. What is overfitting and how do you prevent it?
2. Explain the bias-variance tradeoff
3. Difference between supervised, unsupervised, and reinforcement learning
4. How would you deploy an ML model to production?
5. What is the transformer architecture? How do attention mechanisms work?
6. Explain precision vs recall vs F1-score
7. What are embeddings and how are they used?

#### General CS Discussion Topics (Karat favorites)
8. Process vs Thread — shared memory, communication methods
9. Stack vs Heap — memory allocation
10. REST vs GraphQL tradeoffs
11. How would you test an API?
12. What is garbage collection?
13. SQL vs NoSQL — when to use which?

**⚡ TIP:** Keep answers to 1-2 minutes max. Don't over-explain. Save time for coding.

---

## 📅 DAY 2 — Saturday, March 21
### Theme: "Build Speed & Confidence" (5-6 hours)

### Morning: More Karat Problems (3 hours)

#### ✅ Problem 5: Words & String Match — 30 min
> Given a string and an array of words, find the first word that can be constructed using the string's letters.
> e.g., string = "balloons", words = ["son", "ball", "friends"] → return "son"

**Pattern:** Character frequency counting (Counter comparison)

---

#### ✅ Problem 6: Substitution Cipher — 30 min
> Given a character mapping, encode a string. Then decode it back.
> Part 1: Encode using the mapping
> Part 2: Decode (reverse the mapping)
> Part 3: Handle edge cases (spaces, punctuation, missing keys)

**Pattern:** Dictionary lookup / reverse dictionary

---

#### ✅ Problem 7: Web Access Log Analysis — 45 min
> Given logs of (timestamp, user_id, resource), find:
> Part 1: The most frequently accessed resource
> Part 2: The earliest and latest access time per user
> Part 3: Resources accessed within a 5-min window per user

**Pattern:** Hash Map aggregation + sorting timestamps

---

#### ✅ Problem 8: Word Search in Matrix (LeetCode 79) — 45 min
> Given a 2D grid of characters and a word, return True if the word exists in the grid.
> Letters must be sequentially adjacent (up/down/left/right). Same cell can't be reused.

**Pattern:** DFS/Backtracking on matrix

---

#### ✅ Problem 9: Course Prerequisites / Topological Sort (LeetCode 207/210) — 45 min
> Given courses and their prerequisites, find a valid order to take all courses.
> Return empty if impossible (cycle detected).

**Pattern:** Build adjacency list + in-degree array, BFS with queue (Kahn's algorithm)

---

### Afternoon: Timed Practice (2 hours)

**Do 2 mock coding sessions, 40 minutes each:**

**Mock 1:** Badge Access + Subdomain Visit Count
- Set a 40-minute timer
- Talk out loud as you code (practice explaining)
- Write test cases before coding

**Mock 2:** Find Rectangle in Matrix + Shared Courses
- Same rules
- If you finish early, optimize or handle edge cases

### Evening: Quick Review (1 hour)
- Re-read your solutions without looking at reference code
- Write down the **pattern** for each (e.g., "Hash Map counting", "Matrix traversal", "Set tracking")
- Review the AI/ML discussion topics one more time

---

## 📅 DAY 3 — Sunday, March 22
### Theme: "Polish & Rest" (3-4 hours, then relax)

### Morning: Final Practice Round (2 hours)

#### Rapid-Fire LeetCode (do 4-5, 20 min each):
| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | Two Sum | Easy | Hash Map |
| 49 | Group Anagrams | Medium | Hash Map + Sorting |
| 238 | Product of Array Except Self | Medium | Prefix/Suffix |
| 215 | Kth Largest Element | Medium | Heap / Quickselect |
| 221 | Maximal Square | Medium | DP on Matrix |

### Afternoon: Interview Simulation (1 hour)

Do a **full 60-minute simulation:**
1. (5 min) Practice your intro: "Hi, I'm ___, I'm an AI Engineer with experience in..."
2. (10 min) Answer 3 discussion questions out loud (pick from the list above)
3. (40 min) Solve 2 coding problems end-to-end with talking
4. (5 min) Prepare 2-3 questions to ask the interviewer

### Evening: Logistics & Rest

- [ ] Test your webcam and microphone
- [ ] Check Karat platform link works (they'll send you one)
- [ ] Have a notepad/scratch paper ready
- [ ] Prepare your coding environment (Karat has a built-in editor, but know your Python well)
- [ ] Get a good night's sleep!

---

## 🧠 Cheat Sheet: Patterns to Remember

| Pattern | When to Use | Python Shortcut |
|---------|-------------|-----------------|
| **Hash Map counting** | Frequencies, aggregation | `collections.Counter()` |
| **Hash Set tracking** | Membership, dedup | `set()`, `add()`, `discard()` |
| **defaultdict** | Group by key | `collections.defaultdict(list)` |
| **Matrix traversal** | Grid problems | Nested `for r in range(rows)` |
| **Sliding Window** | Subarray/window problems | Two pointers, expand/shrink |
| **DFS/BFS** | Graph, tree, grid paths | Recursion or `deque` |
| **Topological Sort** | Dependencies, ordering | In-degree + BFS with `deque` |
| **Two Pointers** | Sorted array, palindromes | `left, right = 0, len-1` |
| **Sorting + Hash** | Group anagrams, matching | `sorted()` as key |
| **String split** | Parsing logs/domains | `.split(".")`, `.split()` |

---

## 💡 Interview Day Tips

1. **Talk constantly** — Silence is your enemy in Karat interviews
2. **Clarify before coding** — Ask about edge cases, input constraints
3. **Start with brute force** — Say "I'll start simple, then optimize"
4. **Test with examples** — Walk through a small test case after coding
5. **Don't panic on Part 2** — If stuck, explain your approach verbally
6. **Time management** — Don't spend >20 min on Part 1; leave time for Part 2
7. **Correctness > Optimization** — A working O(n²) beats a broken O(n)
8. **Use Python idioms** — `Counter`, `defaultdict`, list comprehensions, `enumerate`

---

## 🔗 Quick Reference Links

- LeetCode Karat tag: `leetcode.com/company/karat/`
- LeetCode 811 (Subdomain Visit Count): `leetcode.com/problems/subdomain-visit-count/`
- LeetCode 79 (Word Search): `leetcode.com/problems/word-search/`
- LeetCode 207 (Course Schedule): `leetcode.com/problems/course-schedule/`
- LeetCode 215 (Kth Largest): `leetcode.com/problems/kth-largest-element-in-an-array/`

---

*Good luck! You've got this. 💪*