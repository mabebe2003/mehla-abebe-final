# Development Log – The Torchbearer

**Student Name:** ____Mehla Abebe___
**Student ID:** ________133875531____

---
## Entry 1 – [05-12-2025]: Initial Plan

I plan on writing a rough draft for the read me to map out the problem conceptually. 
Once I have a rough draft of the read me, I will tackle the technical coding questions
by starting with a divide and conquer approach. The problems will be broken down into 
smaller sub problems to solve the entire whole. The hardest part is combining these smaller 
pieces to create a larger solution. 
---
## Entry 2 – [05-13-2025]: [Errors in the implemented function]

(4:00 pm) updated README and select sources 

Assumption #1  I forgot to remove duplicate nodes in the sources list. To fix the issue
I implemeneted a simple for loop to check if the node being added was already in the sources list. 

(8:00 pm) Explain problem/ selected sources/ dijkstra/precompuation

Assumption #2  I mistaked look up time complexity and cost per run to be the same thing.
Look up time complexity is asking the complexity of looking up the computed values. While cost per run,
asks the time complexity of running one Dijkstra. 

---

## Entry 3 – [05-14-2025]: [Implementing the optimal route function]

(12:00 pm) Implemented optimal route function without pruning. 
Assumption#1 I initailly used best as a list. Since the program required it to be returned as a touple, I convereted it to one while returning the value.
---

## Entry 4 – [05-14-2025]: Post-Implementation Reflection

The one thing I would change would be work on better exception handling better.Some lines of codes were delicate and might have risked a crash if inputs were unique. 

For instance,  relics_remaining.remove (chosen_relic) and relics_visited_order.append (chosen_relic) in explore function remove and append by node instead of index which can be risky if there are duplicates. 
---

## Final Entry – [05-14-2026]: Time Estimate

| Part | Estimated Hours |

| Part 1: Problem Analysis | 1hr|
| Part 2: Precomputation Design | 6hrs|
| Part 3: Algorithm Correctness | 1hr |
| Part 4: Search Design |2 hr|
| Part 5: State and Search Space |5hr|
| Part 6: Pruning |0.5hr |
| Part 7: Implementation |1hr|
| README and DEVLOG writing | 3hr |
| **Total** |~ 20hrs|
