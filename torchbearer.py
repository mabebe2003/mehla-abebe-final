"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ____Mehla Abebe_______________________
Student ID:   _____133875531________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq
import sys

# =============================================================================
# PART 1
# =============================================================================

def explain_problem():

    response = """ 
    Why a single shortest-path run from S is not enough:
  A single shortest path run from S is not enough because the algorithm 
  must make the decision of not only getting from S to T with minimum fuel cost 
  but also travel through specific nodes (the chambers) before reaching T.

    What decision remains after all inter-location costs are known:
  How can the engine run from S to T while entering all nodes in M 
  atleast once with the minimum cost ?  

    Why this requires a search over orders (one sentence):
  Different order of nodes must be searched to find the most optimal path 
  that reduces the fuel cost. """
    
    return response

# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):

    # add all the source nodes to a list 
    sources = [spawn] 

    for x in relics: 
        # prevent duplicates
        if x not in sources:
            sources.append(x)

    return sources

def run_dijkstra(graph, source):
        
    #helper function to calcuate minimum path from each source node 

    # Min-heap (priority queue) storing pairs of (distance, node)
        pq = []
        dist = {key: float('inf') for key in graph}


    # Distance from source to itself is 0
        dist[source] = 0
        heapq.heappush(pq, (0, source))

    # Process the queue until all reachable vertices are finalized
        while pq:
            d, u = heapq.heappop(pq)

        #skip maximized distances
            if d > dist[u]:
                continue

        # if node u exists in the graph 
            if u in graph:
            # Explore all neighbors of the current vertex
                for v, w in graph[u]:
                # if v has not been added to dist add it and assign infinity
                    if (v not in dist):
                        dist[v] = float('inf')

            # If we found a shorter path to v through u, update it
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v)) 
        return dist

def precompute_distances(graph, spawn, relics, exit_node):

    source = select_sources (spawn, relics, exit_node)
    main_dict = {} # holds set of sources with their respective mininum path cost

    # for each source compute the minimum shortest path to every other node 
    for x in source:
    
        main_dict[x] = run_dijkstra(graph, x)  
    
    return main_dict

# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():

    response = """ 
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
Having the correct shortest path distances is important because inaccurate values can increase the fuel cost of the torchbearer by providing a non-optimal route. """
    return response


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    response = """ 
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

It must search different order of nodes that produce the most optimal solution while preventing visited relic chambers that add cost from being revisited."""
    return response


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):

    current_loc = spawn
    relics_remaining = relics 
    cost_so_far = 0
    relics_visited_order = []
    best = [float('inf'),  []]

    # Call helper function to disover optimal route 
    # Return (float('inf'), []) if no valid route exists.
    optimal_route = _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best)

    return optimal_route


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    
    if not relics_remaining:
        #if there exists a valid route from current node to exit
        if dist_table[current_loc] [exit_node] != float('inf') :
            total_cost = cost_so_far + dist_table[current_loc] [exit_node]
        #if cost so far is better update the best solution tracker list
        # best[0] cost , best [1] path
            if total_cost < best [0]:
                best [0] = total_cost
                best [1]= relics_visited_order[:] #store copy 
        return 

    for i in range(0, len(relics_remaining)):

        # if there isnt a valid route from the current location to relic skip an iteration 
        if dist_table[current_loc] [relics_remaining[i]] == float('inf') :
            continue
        
        else: 
            new_current_loc = relics_remaining[i]
            new_cost_so_far =  cost_so_far + dist_table[current_loc][new_current_loc]

            #mark the chosen relic as visited 
            chosen_relic = relics_remaining[i]
            relics_remaining.remove (chosen_relic)
            relics_visited_order.append (chosen_relic)

            #run recursive 
            _explore(dist_table,  new_current_loc, relics_remaining, relics_visited_order,
             new_cost_so_far, exit_node, best)
            
            #backtrack 
            relics_remaining.insert (i, relics_visited_order.pop() )



# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
