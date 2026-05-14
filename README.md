# The Torchbearer

**Student Name:** ___Mehla Abebe___
**Student ID:** _____133875531___
**Course:** CS 460 – Algorithms | Spring 2026

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**

  A single shortest path run from S is not enough because the algorithm 
  must make the decision of not only getting from S to T with minimum fuel cost 
  but also travel through specific nodes (the chambers) before reaching T.

- **What decision remains after all inter-location costs are known:**

  How can the engine run from S to T while entering all nodes in M 
  atleast once with the minimum cost ?  

- **Why this requires a search over orders (one sentence):**
  
  Different order of nodes must be searched to find the most optimal path 
  that reduces the fuel cost. 

---
## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
| S | As the starting node, it is important to know the distance from S to calcuate min cost. |
| M (B,C,D) | As the chambers that need to be visited, it is important to know the distance from M to calcuate min cost |

### Part 2b: Distance Storage

| Data structure name | PRIORITY QUEUE |
| What the keys represent | Node identifier |
| What the values represent | The best currently known minimum distance from the source node to that node.|
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Precomputing the distance can allow for an O(1)/instant lookup since the computing has already been done. |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** 
  Given a sequence of nodes u1, u2, ..., uk and want to find the shortest path from u1 to uk. 
  This could be done by running k-1 instances of Dijkstra's algorithm, one for each pair of adjacent vertices. 
  In this case given the nodes S, B, C, D, T, Dijkstra is ran four times from each source node S, B, C, D. 

- **Cost per run:**
  O((E+V)*logV) where E is number of edges and V is number of vertice

- **Total complexity:**  
  O( k((E+V)*logV) ) where k is the number of nodes in the sequence

- **Justification:** 
  Since it runs k-1 times in the for loop, k-1 will be multiplied by the usual time complexity O((E+V)*logV).
---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
