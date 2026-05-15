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

- **For nodes already finalized (in S):**
  For every node v in S, dist[v] is the finalized minimum fuel cost to move from the source node to the node v after relaxation is completed. 

- **For nodes not yet finalized (not in S):**
   For every node u not in S, dist[u] is the SO FAR KNOWN minimum fuel cost to move from the source node to the node u while relaxation is not fully completed. However, all the dist values from the source node up to the node u have been finalized already.  
### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  - Invariant for nodes finalized 
  At the start of the iteration S is empty because nothing has been finalized yet so the invariant is trivially true.
  - Invariants for nodes not finalized
  At the start of the iteration, for non finalized nodes u (excluding source), the dist[u] is given as 
  infinity which represents the fact that the paths are still unknown. 

- **Maintenance : why finalizing the min-dist node is always correct:**

Let's say to have a finalized shorter path to u, it must go through some node k not in S. 
But since we only have non-negative edge weights, a shorter path going through k, means that k must be chosen before u which is a contradiction. 

Finalizing min-dist node is always correct because any other path which always contains non-negative edge weights would only increase the cost. 

- **Termination : what the invariant guarantees when the algorithm ends:**
  The invaraint guranatees that all paths have been finalized meaning the relaxation process is empty. This happens when the priority queue which holds non-finalized paths is empty.

### Part 3c: Why This Matters for the Route Planner
Having the correct shortest path distances is important because inaccurate values can increase the fuel cost of the torchbearer by providing a non-optimal route.

---
## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:**  Greedy picks the node with shortest path distance for every point in the route making locally optimal decisions that can lead to a non-optimal global solution. 
- **Counter-example setup:** For instance from the illustration example 
| From \ To | B   | C   | D   | T   |
|-----------|-----|-----|-----|-----|
| S         | 1   | 2   | 2   | --  |
| B         | --  | 100 | 1   | 1   |
| C         | 1   | --  | 100 | 1   |
| D         | 1   | 1   | --  | 100 |
Start S
Shortest path from S is B = 1
Shortest path from B is D = 1 
Shortest path from D is B & C (let's choose B) = 1
Shortest path from B is D = 1
Shortest path from D is B & C (let's choose C) = 1
Shortest path from C is B & T (let's choose T) = 1
End T
- **What greedy picks:**
S-> B -> D -> B -> D -> C -> T  = 6
- **What optimal picks:** 
S-> B -> D -> C -> T  = 4
- **Why greedy loses:** The greedy solution fails to notice that some of the shortest path distances available at each route point loop us back into relics that have already been visited which can be a waste. 

### What the Algorithm Must Explore

It must search different order of nodes that produce the most optimal solution while preventing visited relic chambers that add cost from being revisited.
---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |

| Current location | current_loc| node of a char value | current node being expanded as a route  |
| Relics already collected | relics_visited_order| list of char values | relic chambers already visited and examined for path cost|
| Fuel cost so far | cost_so_far| float | so far calcuated cost for route |

### Part 5b: Data Structure for Visited Relics 

| Property | Your answer |
| Data structure chosen | list |
| Operation: check if relic already collected | Time complexity: O(n × n!) |
| Operation: mark a relic as collected | Time complexity: O(n × n!)|
| Operation: unmark a relic (backtrack) | Time complexity: O(K ^ N), where ‘K’ is the number of times the function calls itself. N is the depth |
| Why this structure fits | A list works best because it can store an ordered collection of items (relics) |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** given k chambers there is a worst case k! order to be considered.
- **Why:** There are n! ways to arrange n items in a full permutation. 

---
## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** best known cost so far 
- **When it is used:** partial new cost for the new path
- **What it allows the algorithm to skip:** It skips exploring the new path through recursion.

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** relics visited so far and path cost of relics visited so far. 
- **What the lower bound accounts for:** cost for remaining routes that are yet to be explored and/or cost to exit node. 
- **Why it never overestimates:** Pruning keeps it from over etimating by comparing cost so far to the lower bound estimate cost. 

### Part 6c: Pruning Correctness
The pruning condition is safe because if the new_cost_so_far being the partial cost calculation exceeds or equals the best known total cost best[0] then it is not worth exploring that path. 

This works because the non negative edge weights will only increase the cost from now on hence why we skip the current path. 

---

## References

https://news.ycombinator.com/item?id=41947355
https://medium.com/@vikramsetty169/time-complexity-of-dijkstras-algorithm-ed4a068e1633
https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python
https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php
https://stackoverflow.com/questions/7314718/finding-a-shortest-path-that-passes-through-some-arbitrary-sequence-of-nodes.
https://youtu.be/Kv2Y4rLJO1U?si=pG_5Cmat3SlaptGN.
https://www.geeksforgeeks.org/dsa/write-a-c-program-to-print-all-permutations-of-a-given-string/.
https://dev.to/devcorner/blog-3-dfs-pattern-path-exploration-connectivity-components-47af.

