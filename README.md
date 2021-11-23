# Algorithms

A collection of common algorithms.

| Algorithm | Wikipedia | time-complexity |
|--------------|:-----:|-----------:|
| *Dynamic Programming* |||
| [knapsack.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/knapsack.py) | [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) | O(n ⋅ W) |
| [edit_distance.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/edit_distance.py) | [Edit distance](https://en.wikipedia.org/wiki/Edit_distance) | O(n ⋅ m) |
| [bellman_ford.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/bellman_ford.py) | [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) | O(n ⋅ m) |
| [sieve_of_eratosthenes.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/sieve_of_eratosthenes.py) | [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) | O(n ⋅ log log n) |
| [robot_paths.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/robot_paths.py) | / | O(n²)
| [subset_sum.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/subset_sum.py) | [Subset sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem) | O(n ⋅ W), [pseudo-polynomial](https://en.wikipedia.org/wiki/Pseudo-polynomial_time) |
| [alarm_problem.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/alarm_problem.py) | / | O(n) |
| [snakes_on_a_grid.py](https://github.com/YannickSpoerl/algorithms/blob/main/dynamic_programming/snakes_on_a_grid.py) | / | O(n ⋅ m) |
| *Greedy Algorithms* |||
| [dijkstra.py](https://github.com/YannickSpoerl/algorithms/blob/main/greedy/dijsktra.py) | [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) | O(n²) |
| [kruskal.py](https://github.com/YannickSpoerl/algorithms/blob/main/greedy/kruskal.py) | [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) | O(m log m) |
| [huffman.py](https://github.com/YannickSpoerl/algorithms/blob/main/greedy/huffman.py) | [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) | O(n log n) |
| [check_bipartiteness.py](https://github.com/YannickSpoerl/algorithms/blob/main/greedy/check_bipartiteness.py) | [Bipartite graph](https://en.wikipedia.org/wiki/Bipartite_graph) | O(n + m) |
| *Network-Flow Algorithms* |||
| [edmonds_karp.py](https://github.com/YannickSpoerl/algorithms/blob/main/network_flow/edmonds_karp.py) | [Edmonds-Karp](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm) | O(n ⋅ m²) |
| *Matching Algorithms* |||
| [gale_shapley.py](https://github.com/YannickSpoerl/algorithms/blob/main/matching/gale_shapley.py) | [Gale-Shapley](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm) | O(n²) |

**Disclaimer 1:** Each algorithm uses its own data-structures, even when they are identical to those of other
algorithms. Thats on purpose.

**Disclaimer 2:** Of course there might be errors or erroneous behaviour on edge-cases. I tested to some extend, but not
exhaustingly.

**Disclaimer 3:** The complexities given in the table are mostly the complexities of the flavour of implementation, not
necessarily the actual complexity for my specific implementation. Therefore actual runtimes might stray from the given
ones.

**Disclaimer 4:** Invokation of algorithms always assumes well-formed input, there is no input-validation (syntactically
or semantically) whatsoever.