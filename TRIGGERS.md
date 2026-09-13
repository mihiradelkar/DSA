# 🔑 Pattern Triggers — problem cue → technique

The single most valuable artifact for pattern automaticity. When you see a problem, this is the
map from "what it says" to "what to reach for." Add your own lines as you solve — the ones *you*
write from your own struggles stick best.

| # | Pattern | Trigger (what the problem looks like) | Technique |
|---|---|---|---|
| 1 | Arrays & Hashing | Dedup / frequency / "seen before?" / complement | Hash map or set for O(1) lookup |
| 2 | Two Pointers | Sorted array, palindrome, pair/triple summing to target | Converge from both ends |
| 3 | Stack | Matching, undo, "nearest greater/smaller to the..." | LIFO stack / monotonic stack |
| 4 | Binary Search | Sorted input, OR "min/max value that satisfies a condition" | Halve the search/answer space |
| 5 | Sliding Window | Longest/shortest **contiguous** subarray/substring with a constraint | Grow right, shrink left; track window state |
| 6 | Linked List | Reorder / detect cycle / nth-from-end / in-place reverse | Dummy head, fast & slow pointers |
| 7 | Trees | "for each node..." / paths / levels / subtree property | DFS recursion (combine children) or BFS (levels) |
| 8 | Tries | Prefix search, autocomplete, dictionary of words | Trie of char nodes |
| 9 | Heap / PQ | Top-K, running median, repeatedly grab min/max | Min/max heap (two heaps for median) |
| 10 | Backtracking | "all combinations / permutations / subsets / partitions" | choose → recurse → un-choose |
| 11 | Graphs | Grid or nodes+edges; connectivity, shortest unweighted, ordering | BFS/DFS; topo sort for ordering; union-find for groups |
| 12 | Advanced Graphs | **Weighted** shortest path, minimum spanning cost | Dijkstra (weighted SP), Prim/Kruskal (MST) |
| 13 | 1-D DP | Count ways / min-max over a sequence, overlapping subproblems | Define dp[i], recurrence, base case |
| 14 | 2-D DP | Two strings/sequences, or grid with choices at each cell | dp[i][j] table; match-vs-skip decisions |
| 15 | Greedy | Local best choice seems to give global best; scheduling | Sort + sweep; prove no future regret |
| 16 | Intervals | Overlaps, merging, scheduling, "can attend all?" | Sort by start (or end), then sweep |
| 17 | Math & Geometry | Simulate a process, in-place matrix transform, numeric pattern | Careful indexing / layer-by-layer / digit math |
| 18 | Bit Manipulation | Pairs cancel, count bits, sets as masks, no extra space | XOR, masks, shifts, `n & (n-1)` |

## My own triggers (add as you solve)

- _e.g. "asked for k-th smallest in a BST → in-order traversal, stop at k"_
-
-
