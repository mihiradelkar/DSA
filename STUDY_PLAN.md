# 🎯 DSA Mastery Plan — NeetCode 150 → Striver A2Z

**Owner:** Mihir · **Target:** Meta / Google · **Started:** 2026-09-13

**Goal:** Not "finish the list." The goal is **pattern automaticity** — see a problem,
recognize the pattern within 60 seconds, and know the technique before writing code.
That only comes from **repetition + spaced review**. We will run NeetCode 150 in
[roadmap](https://neetcode.io/roadmap) order over multiple passes, then expand to Striver A2Z.

---

## Where you stand today

You already have **~169 problems** solved in this repo. Cross-referenced against the real
NeetCode 150 (matched by problem slug, not folder number):

| | Count |
|---|---|
| **NeetCode 150 confirmed done** | **68 / 150 (45%)** |
| Fully complete patterns | Two Pointers (5/5), 2-D DP (11/11) |
| Coldest patterns (do first) | Tries 0/3 · Bit Manip 1/7 · Intervals 1/6 · Stack 1/7 |
| Strong already | 1-D DP 9/12 · Graphs 6/13 · Heap 5/7 |

> The 45% is *confirmed by exact match*. Real recognition is higher — you've solved harder
> variants of many "missing" anchors (e.g. Jump Game is `[ ]` here but you did Jump Game
> III–IX). For **mastery**, that doesn't matter: we do every problem anyway until the
> pattern is reflex. A `[x]` below means "solved once, long ago" — not "mastered."

---

## The mastery method — 3 passes per problem

A problem isn't "done" — it has a **confidence level**. Track it with the checkbox + a tag:

- `[ ]` **P0** — never solved, or fully cold.
- `[~]` **P1** — solved it, but needed hints / >30 min / peeked. *Needs review.*
- `[x]` **P2** — solved clean, first try, but slowly.
- `[x] ⭐` **P3 (mastered)** — solved in target time, explained out loud, no hesitation. **Done.**

**Spaced repetition:** any problem that lands at P1 gets re-done at **Day 1 → Day 3 → Day 7 → Day 21**.
If it's still shaky, it stays in rotation. When you can look at it and *narrate the approach in
under a minute without solving*, it's mastered — retire it.

**Per-problem loop (the "pro" reps):**
1. Read problem. **Before coding**, say the pattern + technique out loud (or write it).
2. Solve. Talk through complexity + edge cases as if in an interview.
3. If you struggled → mark `[~]`, add to the spaced queue.
4. Every few problems, ask: *"what's the one-line trigger that maps this problem to this pattern?"*
   Collect these in `TRIGGERS.md` — that sheet is what makes patterns transfer.

**Target times (Pass 2+):** Easy ≤ 10 min · Medium ≤ 25 min · Hard ≤ 40 min.

---

## Phase plan

### Phase 1 — NeetCode 150, roadmap order (Passes 1–2)
Go **top to bottom** through the checklist below — it's already in NeetCode's dependency order
(each pattern builds on the ones above). Do the whole pattern before moving on: cold problems
first, then re-verify the `[x]` ones are actually fast. **Don't skip ahead** — the order is the
point; Trees assumes Two Pointers, Graphs assumes Trees, 2-D DP assumes 1-D DP.

- **Pass 1 (breadth):** every problem to at least P2. Coldest patterns first within reason.
- **Pass 2 (speed):** re-run under target times, out loud. This is where interviews are won.

### Phase 2 — NeetCode 150, mastery (Pass 3)
Only the problems still marked `[~]`. Grind the spaced queue until every one hits ⭐.
**Exit criteria:** you can be handed any random NC150 problem and name the pattern in < 60s.

### Phase 3 — Striver A2Z expansion (~455 problems)
Once NC150 is reflex, expand breadth with the [Striver A2Z Sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/).
It covers everything NC150 does plus depth NC skips (advanced arrays, recursion depth,
bit tricks, harder graphs/DP, and fundamentals like sorting/heaps from scratch). Because
NC150 ≈ 60% of A2Z's patterns, you'll fly through the first half. Structure:
- Step through A2Z in its own order; **skip-with-a-quick-recall-check** anything NC150 already made reflex.
- Focus new reps on: Step 3 (sorting internals), Step 7 (deep recursion), Step 14 (bit manip),
  Step 16 (greedy depth), Step 17–18 (advanced DP), Step 19 (tries), Step 20 (strings/KMP).
- Same 3-pass + spaced-repetition method. Tracked in **[STRIVER_A2Z.md](STRIVER_A2Z.md)** — all 18 steps, ~442 problems, already cross-referenced against your repo (73 auto-matched).

> **Note:** "Striver 400" most closely maps to the **A2Z sheet (~455)**. If you meant the
> shorter **[SDE Sheet (~191)](https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/)**
> (faster, interview-focused, less foundational), say so and I'll build that variant instead.

---

## Cadence

| | Weekday (~1–1.5 hr) | Weekend (~3 hr) |
|---|---|---|
| **Volume** | 3–4 problems | 6–8 problems |
| **Focus** | 1 new pattern block + spaced-queue review | finish pattern + 1 Hard + mock-style timed set |
| **Always** | talk out loud · write the trigger · log struggles as `[~]` | |

At ~4 problems/weekday this is a **~6–7 week** run through Phase 1+2. Sustainable cadence beats
your old burst (127 in April → 9 in June → stop). **Consistency is the whole game.**

Every accepted submission auto-commits here via LeetSync — so this file's `[x]` marks and your
green commit graph should move together. Update the checkboxes as you go; it's your dashboard.

---

## ✅ NeetCode 150 — roadmap-ordered checklist

_Legend: `[ ]` todo · `[~]` needs review · `[x]` solved · add `⭐` when mastered.
Pre-checked `[x]` = already in your repo (linked). `E`/`M`/`H` = difficulty._

### 1. Arrays & Hashing — 2/9
> **Trigger:** Store/count/lookup in O(1) -> hash map/set. Dedup, frequency, complement.

- [ ] `E` [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [ ] `E` [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [ ] `E` [Two Sum](https://leetcode.com/problems/two-sum/)
- [ ] `M` [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [x] `M` [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — solved: [`347-top-k-frequent-elements`](347-top-k-frequent-elements)
- [ ] `M` [Encode And Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
- [ ] `M` [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [ ] `M` [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
- [x] `M` [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — solved: [`128-longest-consecutive-sequence`](128-longest-consecutive-sequence)

### 2. Two Pointers — 5/5
> **Trigger:** Sorted array / palindrome / pair-sum -> converge from both ends.

- [x] `E` [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — solved: [`125-valid-palindrome`](125-valid-palindrome)
- [x] `M` [Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — solved: [`167-two-sum-ii-input-array-is-sorted`](167-two-sum-ii-input-array-is-sorted)
- [x] `M` [3Sum](https://leetcode.com/problems/3sum/) — solved: [`15-3sum`](15-3sum)
- [x] `M` [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — solved: [`11-container-with-most-water`](11-container-with-most-water)
- [x] `H` [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) — solved: [`42-trapping-rain-water`](42-trapping-rain-water)

### 3. Stack — 1/7
> **Trigger:** Match/undo/nearest-greater -> LIFO. Monotonic stack for next-greater/smaller.

- [ ] `E` [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [ ] `M` [Min Stack](https://leetcode.com/problems/min-stack/)
- [ ] `M` [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- [ ] `M` [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [x] `M` [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) — solved: [`739-daily-temperatures`](739-daily-temperatures)
- [ ] `M` [Car Fleet](https://leetcode.com/problems/car-fleet/)
- [ ] `H` [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

### 4. Binary Search — 2/7
> **Trigger:** Sorted or monotonic answer space -> halve each step. 'Min value that works' = binary search on answer.

- [ ] `E` [Binary Search](https://leetcode.com/problems/binary-search/)
- [ ] `M` [Search A 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [ ] `M` [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [x] `M` [Find Minimum In Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) — solved: [`153-find-minimum-in-rotated-sorted-array`](153-find-minimum-in-rotated-sorted-array)
- [x] `M` [Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — solved: [`33-search-in-rotated-sorted-array`](33-search-in-rotated-sorted-array)
- [ ] `M` [Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/)
- [ ] `H` [Median Of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

### 5. Sliding Window — 4/6
> **Trigger:** Contiguous subarray/substring with a constraint -> grow right, shrink left.

- [ ] `E` [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [x] `M` [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — solved: [`3-longest-substring-without-repeating-characters`](3-longest-substring-without-repeating-characters)
- [x] `M` [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) — solved: [`424-longest-repeating-character-replacement`](424-longest-repeating-character-replacement)
- [ ] `M` [Permutation In String](https://leetcode.com/problems/permutation-in-string/)
- [x] `H` [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — solved: [`76-minimum-window-substring`](76-minimum-window-substring)
- [x] `H` [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) — solved: [`239-sliding-window-maximum`](239-sliding-window-maximum)

### 6. Linked List — 3/11
> **Trigger:** Pointer manipulation -> dummy head, fast/slow, reverse in place.

- [ ] `E` [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [x] `E` [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — solved: [`21-merge-two-sorted-lists`](21-merge-two-sorted-lists)
- [ ] `M` [Reorder List](https://leetcode.com/problems/reorder-list/)
- [ ] `M` [Remove Nth Node From End Of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [x] `M` [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) — solved: [`138-copy-list-with-random-pointer`](138-copy-list-with-random-pointer)
- [x] `M` [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) — solved: [`2-add-two-numbers`](2-add-two-numbers)
- [ ] `E` [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [ ] `M` [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
- [ ] `M` [Lru Cache](https://leetcode.com/problems/lru-cache/)
- [ ] `H` [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [ ] `H` [Reverse Nodes In K Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

### 7. Trees — 3/15
> **Trigger:** Recurse: solve for children, combine. BFS for levels, DFS for paths.

- [ ] `E` [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [ ] `E` [Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [x] `E` [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — solved: [`543-diameter-of-binary-tree`](543-diameter-of-binary-tree)
- [ ] `E` [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- [ ] `E` [Same Tree](https://leetcode.com/problems/same-tree/)
- [ ] `E` [Subtree Of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- [ ] `M` [Lowest Common Ancestor Of A Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [ ] `M` [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [x] `M` [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) — solved: [`199-binary-tree-right-side-view`](199-binary-tree-right-side-view)
- [ ] `M` [Count Good Nodes In Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)
- [ ] `M` [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [ ] `M` [Kth Smallest Element In A Bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [ ] `M` [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [x] `H` [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — solved: [`124-binary-tree-maximum-path-sum`](124-binary-tree-maximum-path-sum)
- [ ] `H` [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

### 8. Tries — 0/3
> **Trigger:** Prefix / word lookup / autocomplete -> trie of char nodes.

- [ ] `M` [Implement Trie Prefix Tree](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [ ] `M` [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- [ ] `H` [Word Search Ii](https://leetcode.com/problems/word-search-ii/)

### 9. Heap / Priority Queue — 5/7
> **Trigger:** Top-K / running median / repeated min-max -> heap.

- [ ] `E` [Kth Largest Element In A Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [x] `E` [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) — solved: [`1127-last-stone-weight`](1127-last-stone-weight)
- [x] `M` [K Closest Points To Origin](https://leetcode.com/problems/k-closest-points-to-origin/) — solved: [`1014-k-closest-points-to-origin`](1014-k-closest-points-to-origin)
- [ ] `M` [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [x] `M` [Task Scheduler](https://leetcode.com/problems/task-scheduler/) — solved: [`621-task-scheduler`](621-task-scheduler)
- [x] `M` [Design Twitter](https://leetcode.com/problems/design-twitter/) — solved: [`355-design-twitter`](355-design-twitter)
- [x] `H` [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) — solved: [`295-find-median-from-data-stream`](295-find-median-from-data-stream)

### 10. Backtracking — 4/9
> **Trigger:** Enumerate all combos/perms/subsets -> choose, recurse, un-choose.

- [x] `M` [Subsets](https://leetcode.com/problems/subsets/) — solved: [`78-subsets`](78-subsets)
- [ ] `M` [Combination Sum](https://leetcode.com/problems/combination-sum/)
- [ ] `M` [Permutations](https://leetcode.com/problems/permutations/)
- [ ] `M` [Subsets Ii](https://leetcode.com/problems/subsets-ii/)
- [x] `M` [Combination Sum Ii](https://leetcode.com/problems/combination-sum-ii/) — solved: [`40-combination-sum-ii`](40-combination-sum-ii)
- [x] `M` [Word Search](https://leetcode.com/problems/word-search/) — solved: [`79-word-search`](79-word-search)
- [ ] `M` [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- [x] `M` [Letter Combinations Of A Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) — solved: [`17-letter-combinations-of-a-phone-number`](17-letter-combinations-of-a-phone-number)
- [ ] `H` [N Queens](https://leetcode.com/problems/n-queens/)

### 11. Graphs — 6/13
> **Trigger:** Grid/connections -> BFS/DFS. Shortest unweighted = BFS. Cycle/order = topo sort.

- [ ] `M` [Number Of Islands](https://leetcode.com/problems/number-of-islands/)
- [ ] `M` [Clone Graph](https://leetcode.com/problems/clone-graph/)
- [x] `M` [Max Area Of Island](https://leetcode.com/problems/max-area-of-island/) — solved: [`695-max-area-of-island`](695-max-area-of-island)
- [ ] `M` [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [x] `M` [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) — solved: [`130-surrounded-regions`](130-surrounded-regions)
- [x] `M` [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — solved: [`1036-rotting-oranges`](1036-rotting-oranges)
- [ ] `M` [Walls And Gates](https://leetcode.com/problems/walls-and-gates/)
- [x] `M` [Course Schedule](https://leetcode.com/problems/course-schedule/) — solved: [`207-course-schedule`](207-course-schedule)
- [ ] `M` [Course Schedule Ii](https://leetcode.com/problems/course-schedule-ii/)
- [x] `M` [Redundant Connection](https://leetcode.com/problems/redundant-connection/) — solved: [`684-redundant-connection`](684-redundant-connection)
- [ ] `M` [Number Of Connected Components In An Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- [ ] `M` [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
- [x] `H` [Word Ladder](https://leetcode.com/problems/word-ladder/) — solved: [`127-word-ladder`](127-word-ladder)

### 12. Advanced Graphs — 4/6
> **Trigger:** Weighted shortest path = Dijkstra. MST = Prim/Kruskal. Ordering = topo.

- [x] `H` [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) — solved: [`332-reconstruct-itinerary`](332-reconstruct-itinerary)
- [x] `M` [Min Cost To Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — solved: [`1706-min-cost-to-connect-all-points`](1706-min-cost-to-connect-all-points)
- [x] `M` [Network Delay Time](https://leetcode.com/problems/network-delay-time/) — solved: [`744-network-delay-time`](744-network-delay-time)
- [ ] `H` [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/)
- [ ] `H` [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- [x] `M` [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) — solved: [`803-cheapest-flights-within-k-stops`](803-cheapest-flights-within-k-stops)

### 13. 1-D DP — 9/12
> **Trigger:** Overlapping subproblems on a line -> define dp[i], recurrence, base case.

- [x] `E` [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) — solved: [`70-climbing-stairs`](70-climbing-stairs)
- [x] `E` [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) — solved: [`747-min-cost-climbing-stairs`](747-min-cost-climbing-stairs)
- [x] `M` [House Robber](https://leetcode.com/problems/house-robber/) — solved: [`198-house-robber`](198-house-robber)
- [x] `M` [House Robber Ii](https://leetcode.com/problems/house-robber-ii/) — solved: [`213-house-robber-ii`](213-house-robber-ii)
- [ ] `M` [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [ ] `M` [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [ ] `M` [Decode Ways](https://leetcode.com/problems/decode-ways/)
- [x] `M` [Coin Change](https://leetcode.com/problems/coin-change/) — solved: [`322-coin-change`](322-coin-change)
- [x] `M` [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) — solved: [`152-maximum-product-subarray`](152-maximum-product-subarray)
- [x] `M` [Word Break](https://leetcode.com/problems/word-break/) — solved: [`139-word-break`](139-word-break)
- [x] `M` [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) — solved: [`300-longest-increasing-subsequence`](300-longest-increasing-subsequence)
- [x] `M` [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — solved: [`416-partition-equal-subset-sum`](416-partition-equal-subset-sum)

### 14. 2-D DP — 11/11
> **Trigger:** Two sequences / grid -> dp[i][j] table. Match/skip decisions.

- [x] `M` [Unique Paths](https://leetcode.com/problems/unique-paths/) — solved: [`62-unique-paths`](62-unique-paths)
- [x] `M` [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) — solved: [`1250-longest-common-subsequence`](1250-longest-common-subsequence)
- [x] `M` [Best Time To Buy And Sell Stock With Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) — solved: [`309-best-time-to-buy-and-sell-stock-with-cooldown`](309-best-time-to-buy-and-sell-stock-with-cooldown)
- [x] `M` [Coin Change Ii](https://leetcode.com/problems/coin-change-ii/) — solved: [`518-coin-change-ii`](518-coin-change-ii)
- [x] `M` [Target Sum](https://leetcode.com/problems/target-sum/) — solved: [`494-target-sum`](494-target-sum)
- [x] `M` [Interleaving String](https://leetcode.com/problems/interleaving-string/) — solved: [`97-interleaving-string`](97-interleaving-string)
- [x] `H` [Longest Increasing Path In A Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) — solved: [`329-longest-increasing-path-in-a-matrix`](329-longest-increasing-path-in-a-matrix)
- [x] `H` [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) — solved: [`115-distinct-subsequences`](115-distinct-subsequences)
- [x] `M` [Edit Distance](https://leetcode.com/problems/edit-distance/) — solved: [`72-edit-distance`](72-edit-distance)
- [x] `H` [Burst Balloons](https://leetcode.com/problems/burst-balloons/) — solved: [`312-burst-balloons`](312-burst-balloons)
- [x] `H` [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) — solved: [`10-regular-expression-matching`](10-regular-expression-matching)

### 15. Greedy — 4/8
> **Trigger:** Local optimal -> global optimal. Prove no future regret.

- [x] `M` [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — solved: [`53-maximum-subarray`](53-maximum-subarray)
- [ ] `M` [Jump Game](https://leetcode.com/problems/jump-game/)
- [ ] `M` [Jump Game Ii](https://leetcode.com/problems/jump-game-ii/)
- [x] `M` [Gas Station](https://leetcode.com/problems/gas-station/) — solved: [`134-gas-station`](134-gas-station)
- [x] `M` [Hand Of Straights](https://leetcode.com/problems/hand-of-straights/) — solved: [`876-hand-of-straights`](876-hand-of-straights)
- [x] `M` [Merge Triplets To Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) — solved: [`2026-merge-triplets-to-form-target-triplet`](2026-merge-triplets-to-form-target-triplet)
- [ ] `M` [Partition Labels](https://leetcode.com/problems/partition-labels/)
- [ ] `M` [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)

### 16. Intervals — 1/6
> **Trigger:** Overlaps/scheduling -> sort by start (or end), sweep.

- [ ] `M` [Insert Interval](https://leetcode.com/problems/insert-interval/)
- [x] `M` [Merge Intervals](https://leetcode.com/problems/merge-intervals/) — solved: [`56-merge-intervals`](56-merge-intervals)
- [ ] `M` [Non Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
- [ ] `E` [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- [ ] `M` [Meeting Rooms Ii](https://leetcode.com/problems/meeting-rooms-ii/)
- [ ] `H` [Minimum Interval To Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

### 17. Math & Geometry — 3/8
> **Trigger:** Simulate carefully / find the numeric pattern. In-place matrix tricks.

- [x] `M` [Rotate Image](https://leetcode.com/problems/rotate-image/) — solved: [`48-rotate-image`](48-rotate-image)
- [ ] `M` [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [x] `M` [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) — solved: [`73-set-matrix-zeroes`](73-set-matrix-zeroes)
- [ ] `E` [Happy Number](https://leetcode.com/problems/happy-number/)
- [ ] `E` [Plus One](https://leetcode.com/problems/plus-one/)
- [x] `M` [Powx N](https://leetcode.com/problems/powx-n/) — solved: [`50-powx-n`](50-powx-n)
- [ ] `M` [Multiply Strings](https://leetcode.com/problems/multiply-strings/)
- [ ] `M` [Detect Squares](https://leetcode.com/problems/detect-squares/)

### 18. Bit Manipulation — 1/7
> **Trigger:** XOR cancels pairs. Masks, shifts, n&(n-1) clears lowest set bit.

- [ ] `E` [Single Number](https://leetcode.com/problems/single-number/)
- [ ] `E` [Number Of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [ ] `E` [Counting Bits](https://leetcode.com/problems/counting-bits/)
- [ ] `E` [Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- [ ] `E` [Missing Number](https://leetcode.com/problems/missing-number/)
- [ ] `M` [Sum Of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- [x] `M` [Reverse Integer](https://leetcode.com/problems/reverse-integer/) — solved: [`7-reverse-integer`](7-reverse-integer)

---

## Next actions

1. **Today:** do the 3 coldest patterns' first problems — Tries (`implement-trie-prefix-tree`),
   Bit Manip (`single-number`), Intervals (`insert-interval`). These are your biggest gaps.
2. **Start `TRIGGERS.md`** — one line per pattern as you go. This is the artifact that makes
   patterns transfer between problems.
3. **Weekly:** re-run your spaced queue (the `[~]` problems). Retire ones that hit ⭐.

_Generated 2026-09-13. Update checkboxes as you solve — this file is your dashboard._
