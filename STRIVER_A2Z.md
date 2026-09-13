# 📘 Striver A2Z DSA Sheet — Mastery Tracker

**Owner:** Mihir · **Target:** Meta / Google · **Phase 3** of the plan (after [NeetCode 150](STUDY_PLAN.md))

The [A2Z sheet](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)
is the comprehensive one: ~450 problems across 18 steps, from language basics and sorting
internals all the way to advanced graphs, DP, and string algorithms. It covers everything
NeetCode 150 does **plus** the foundations NC150 skips (sorting from scratch, deep recursion,
bit tricks, KMP/Z-function, MST/SCC, full DP taxonomy).

## How to use this with NeetCode 150

**Don't do these in parallel.** Finish NC150 to reflex first (Phases 1–2). Then run A2Z
top-to-bottom. Because NC150 ≈ 60% of A2Z's patterns, the **first half will fly** — for anything
you've already mastered, do a 60-second recall check and move on; only stop and grind where A2Z
goes deeper. Spend your real reps on the parts NC150 never taught you:

- **Step 2** sorting internals · **Step 7** deep recursion/backtracking · **Step 8** bit manipulation
- **Step 9** infix/prefix/postfix + monotonic stack depth · **Step 15.4–15.6** Bellman-Ford,
  Floyd-Warshall, MST, disjoint-set, bridges, SCC
- **Step 16** the *full* DP taxonomy (subsequences, strings, stocks, LIS, partition/MCM, squares)
- **Step 17** trie+XOR · **Step 18** string algorithms (KMP, Z, Rabin-Karp)

## Same mastery method as NC150

3 passes per problem, spaced repetition on anything shaky (Day 1/3/7/21). Legend below.
_`[ ]` todo · `[~]` needs review · `[x]` solved · add `⭐` when mastered._

## Auto-matched from your repo

Every problem with a known LeetCode equivalent was cross-referenced against your ~174 solved
folders by slug. A pre-checked `[x]` links to your existing solution. **Caveat:** ~40% of A2Z
problems are GFG / Coding-Ninjas-native (no LeetCode slug) — those show unchecked with just a name;
check them off manually as you solve on tuf. This tracker is a faithful reconstruction of the A2Z
structure; reconcile against the live sheet as you go, since tuf occasionally revises it.

## Progress by step

| Step | Auto-matched from repo |
|---|---|
| Step 1 — Learn the Basics | 0/28 |
| Step 2 — Sorting Techniques | 0/7 |
| Step 3 — Arrays [Easy → Medium → Hard] | 12/40 |
| Step 4 — Binary Search | 6/31 |
| Step 5 — Strings [Basic/Medium] | 2/15 |
| Step 6 — Linked List | 3/31 |
| Step 7 — Recursion [Pattern-wise] | 5/25 |
| Step 8 — Bit Manipulation | 1/18 |
| Step 9 — Stacks & Queues | 4/31 |
| Step 10 — Sliding Window & Two Pointer | 4/12 |
| Step 11 — Heaps / Priority Queue | 5/17 |
| Step 12 — Greedy Algorithms | 1/16 |
| Step 13 — Binary Trees | 6/36 |
| Step 14 — Binary Search Trees | 0/16 |
| Step 15 — Graphs | 10/48 |
| Step 16 — Dynamic Programming | 14/55 |
| Step 17 — Tries | 0/7 |
| Step 18 — Strings [Hard] | 0/9 |
| **TOTAL** | **73/442** |

## Step 1 — Learn the Basics — 0/28 matched


**1.1 Language & complexity basics**

- [ ] User Input / Output
- [ ] Data Types
- [ ] If-Else / Switch
- [ ] Arrays, Strings basics
- [ ] For / While loops
- [ ] Functions (pass by value/ref)
- [ ] Time & Space Complexity basics

**1.2 Patterns (logic build-up)**

- [ ] Star / number patterns (1-22)

**1.3 STL / Collections**

- [ ] C++ STL
- [ ] Java Collections

**1.4 Basic Maths**

- [ ] `E` Count Digits
- [ ] `E` Reverse a Number
- [ ] `E` Check Palindrome number
- [ ] `E` GCD / HCF
- [ ] `E` Armstrong Number
- [ ] `E` Print all Divisors
- [ ] `E` Check for Prime

**1.5 Basic Recursion**

- [ ] `E` Print name N times
- [ ] `E` Print 1..N
- [ ] `E` Print N..1
- [ ] `E` Sum of first N
- [ ] `E` Factorial of N
- [ ] `E` Reverse an array (recursion)
- [ ] `E` String palindrome (recursion)
- [ ] `E` [Fibonacci number](https://leetcode.com/problems/fibonacci-number/)

**1.6 Basic Hashing**

- [ ] Hashing theory
- [ ] `E` Count frequency of elements
- [ ] `E` Highest / lowest frequency element

## Step 2 — Sorting Techniques — 0/7 matched


**2.1 Sorting I**

- [ ] `E` Selection Sort
- [ ] `E` Bubble Sort
- [ ] `E` Insertion Sort

**2.2 Sorting II**

- [ ] `M` Merge Sort
- [ ] `E` Recursive Bubble Sort
- [ ] `E` Recursive Insertion Sort
- [ ] `M` Quick Sort

## Step 3 — Arrays [Easy → Medium → Hard] — 12/40 matched


**3.1 Easy**

- [ ] `E` Largest Element
- [ ] `E` Second Largest (no sort)
- [x] `E` [Check if array is sorted](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) — [`1878-check-if-array-is-sorted-and-rotated`](1878-check-if-array-is-sorted-and-rotated)
- [ ] `E` [Remove duplicates from sorted array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [ ] `E` Left rotate array by 1
- [ ] `M` [Left rotate array by D places](https://leetcode.com/problems/rotate-array/)
- [ ] `E` [Move zeros to end](https://leetcode.com/problems/move-zeroes/)
- [ ] `E` Linear Search
- [ ] `E` Union of two sorted arrays
- [ ] `E` [Missing number](https://leetcode.com/problems/missing-number/)
- [x] `E` [Max consecutive ones](https://leetcode.com/problems/max-consecutive-ones/) — [`485-max-consecutive-ones`](485-max-consecutive-ones)
- [ ] `E` [Single number (others twice)](https://leetcode.com/problems/single-number/)
- [ ] `M` Longest subarray sum K (positives)
- [ ] `M` Longest subarray sum K (pos+neg)

**3.2 Medium**

- [ ] `M` [Two Sum](https://leetcode.com/problems/two-sum/)
- [x] `M` [Sort 0s 1s 2s](https://leetcode.com/problems/sort-colors/) — [`75-sort-colors`](75-sort-colors)
- [ ] `E` [Majority Element (>n/2)](https://leetcode.com/problems/majority-element/)
- [x] `M` [Kadane's — Max Subarray Sum](https://leetcode.com/problems/maximum-subarray/) — [`53-maximum-subarray`](53-maximum-subarray)
- [ ] `M` Print subarray with max sum
- [ ] `E` [Stock Buy and Sell](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [ ] `M` [Rearrange by sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/)
- [ ] `M` [Next Permutation](https://leetcode.com/problems/next-permutation/)
- [ ] `E` Leaders in an array
- [x] `M` [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) — [`128-longest-consecutive-sequence`](128-longest-consecutive-sequence)
- [x] `M` [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) — [`73-set-matrix-zeroes`](73-set-matrix-zeroes)
- [x] `M` [Rotate Image 90](https://leetcode.com/problems/rotate-image/) — [`48-rotate-image`](48-rotate-image)
- [ ] `M` [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- [x] `M` [Subarray sum equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — [`560-subarray-sum-equals-k`](560-subarray-sum-equals-k)

**3.3 Hard**

- [ ] `M` [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
- [ ] `M` [Majority Element (n/3)](https://leetcode.com/problems/majority-element-ii/)
- [x] `M` [3 Sum](https://leetcode.com/problems/3sum/) — [`15-3sum`](15-3sum)
- [x] `M` [4 Sum](https://leetcode.com/problems/4sum/) — [`18-4sum`](18-4sum)
- [ ] `M` Largest subarray with 0 sum
- [ ] `H` Subarrays with XOR K
- [x] `M` [Merge Intervals](https://leetcode.com/problems/merge-intervals/) — [`56-merge-intervals`](56-merge-intervals)
- [ ] `M` [Merge two sorted arrays no extra space](https://leetcode.com/problems/merge-sorted-array/)
- [ ] `H` Repeating and missing number
- [ ] `H` Count Inversions
- [ ] `H` [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)
- [x] `M` [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) — [`152-maximum-product-subarray`](152-maximum-product-subarray)

## Step 4 — Binary Search — 6/31 matched


**4.1 BS on 1D arrays**

- [ ] `E` [Binary Search find X](https://leetcode.com/problems/binary-search/)
- [ ] `E` Lower Bound
- [ ] `E` Upper Bound
- [ ] `E` [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- [ ] `E` Floor / Ceil in sorted array
- [x] `M` [First & last occurrence](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) — [`34-find-first-and-last-position-of-element-in-sorted-array`](34-find-first-and-last-position-of-element-in-sorted-array)
- [ ] `E` Count occurrences
- [x] `M` [Search in Rotated Sorted Array I](https://leetcode.com/problems/search-in-rotated-sorted-array/) — [`33-search-in-rotated-sorted-array`](33-search-in-rotated-sorted-array)
- [ ] `M` [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
- [x] `M` [Find min in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) — [`153-find-minimum-in-rotated-sorted-array`](153-find-minimum-in-rotated-sorted-array)
- [ ] `E` How many times array rotated
- [ ] `M` [Single element in sorted array](https://leetcode.com/problems/single-element-in-a-sorted-array/)
- [x] `M` [Find peak element](https://leetcode.com/problems/find-peak-element/) — [`162-find-peak-element`](162-find-peak-element)

**4.2 BS on answers**

- [x] `E` [Square root](https://leetcode.com/problems/sqrtx/) — [`69-sqrtx`](69-sqrtx)
- [ ] `M` Nth root
- [ ] `M` [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [ ] `M` [Min days for M bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
- [ ] `M` [Smallest Divisor given threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)
- [ ] `M` [Capacity to ship in D days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- [x] `E` [Kth Missing Positive](https://leetcode.com/problems/kth-missing-positive-number/) — [`1646-kth-missing-positive-number`](1646-kth-missing-positive-number)
- [ ] `H` Aggressive Cows
- [ ] `H` [Book Allocation / Split array largest sum](https://leetcode.com/problems/split-array-largest-sum/)
- [ ] `H` Painter's Partition
- [ ] `H` Min max distance gas station
- [ ] `H` [Median of two sorted arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [ ] `M` Kth element of two sorted arrays

**4.3 BS on 2D**

- [ ] `E` Row with max 1's
- [ ] `M` [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [ ] `M` [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
- [ ] `M` [Find peak element 2D](https://leetcode.com/problems/find-a-peak-element-ii/)
- [ ] `H` Matrix Median

## Step 5 — Strings [Basic/Medium] — 2/15 matched


**5.1 Basic**

- [ ] `E` [Remove outermost parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)
- [ ] `M` [Reverse words in a string](https://leetcode.com/problems/reverse-words-in-a-string/)
- [ ] `E` [Largest odd number in string](https://leetcode.com/problems/largest-odd-number-in-string/)
- [x] `E` [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) — [`14-longest-common-prefix`](14-longest-common-prefix)
- [ ] `E` [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
- [x] `E` [Rotate string / check rotation](https://leetcode.com/problems/rotate-string/) — [`812-rotate-string`](812-rotate-string)
- [ ] `E` [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

**5.2 Medium**

- [ ] `M` [Sort characters by frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
- [ ] `E` [Max nesting depth of parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)
- [ ] `E` [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- [ ] `M` [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
- [ ] `M` Count substrings
- [ ] `M` [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [ ] `M` Sum of beauty of all substrings
- [ ] `M` Reverse every word

## Step 6 — Linked List — 3/31 matched


**6.1 Singly LL basics**

- [ ] Introduction to LL
- [ ] `E` Insert a node
- [ ] `M` [Delete a node](https://leetcode.com/problems/delete-node-in-a-linked-list/)
- [ ] `E` Length of LL
- [ ] `E` Search element

**6.2 Doubly LL basics**

- [ ] Intro to DLL
- [ ] `E` Insert in DLL
- [ ] `E` Delete in DLL
- [ ] `M` Reverse a DLL

**6.3 Medium LL**

- [ ] `E` [Middle of LL](https://leetcode.com/problems/middle-of-the-linked-list/)
- [ ] `E` [Reverse LL (iterative)](https://leetcode.com/problems/reverse-linked-list/)
- [ ] `E` [Reverse LL (recursive)](https://leetcode.com/problems/reverse-linked-list/)
- [ ] `E` [Detect loop](https://leetcode.com/problems/linked-list-cycle/)
- [ ] `M` [Start of loop](https://leetcode.com/problems/linked-list-cycle-ii/)
- [ ] `M` Length of loop
- [ ] `E` [Palindrome LL](https://leetcode.com/problems/palindrome-linked-list/)
- [ ] `M` [Segregate odd/even nodes](https://leetcode.com/problems/odd-even-linked-list/)
- [ ] `M` [Remove Nth node from end](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [ ] `M` [Delete middle node](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)
- [ ] `M` [Sort a LL](https://leetcode.com/problems/sort-list/)
- [ ] `M` Sort LL of 0s 1s 2s
- [ ] `E` [Intersection of two LL](https://leetcode.com/problems/intersection-of-two-linked-lists/)
- [ ] `M` Add 1 to number as LL
- [x] `M` [Add two numbers as LL](https://leetcode.com/problems/add-two-numbers/) — [`2-add-two-numbers`](2-add-two-numbers)

**6.4 Medium DLL**

- [ ] `M` Delete all occurrences of key in DLL
- [ ] `M` Pairs with given sum in DLL
- [ ] `M` Remove duplicates from sorted DLL

**6.5 Hard LL**

- [ ] `H` [Reverse LL in groups of K](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [x] `M` [Rotate a LL](https://leetcode.com/problems/rotate-list/) — [`61-rotate-list`](61-rotate-list)
- [ ] `M` Flatten a LL
- [x] `M` [Copy LL with random pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) — [`138-copy-list-with-random-pointer`](138-copy-list-with-random-pointer)

## Step 7 — Recursion [Pattern-wise] — 5/25 matched


**7.1 Get strong hold**

- [ ] `M` [Recursive atoi()](https://leetcode.com/problems/string-to-integer-atoi/)
- [x] `M` [Pow(x, n)](https://leetcode.com/problems/powx-n/) — [`50-powx-n`](50-powx-n)
- [ ] `M` [Count good numbers](https://leetcode.com/problems/count-good-numbers/)
- [ ] `M` Sort a stack (recursion)
- [ ] `M` Reverse a stack (recursion)

**7.2 Subsequences pattern**

- [ ] `M` Generate all binary strings
- [ ] `M` [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [x] `M` [Print all subsequences / Power Set](https://leetcode.com/problems/subsets/) — [`78-subsets`](78-subsets)
- [ ] Subsequence patterns (theory)
- [ ] `M` Count subsequences with sum K
- [ ] `M` Check subsequence with sum K
- [ ] `M` [Combination Sum](https://leetcode.com/problems/combination-sum/)
- [x] `M` [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) — [`40-combination-sum-ii`](40-combination-sum-ii)
- [ ] `M` Subset Sum I
- [ ] `M` [Subset Sum II](https://leetcode.com/problems/subsets-ii/)
- [ ] `M` [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
- [x] `M` [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) — [`17-letter-combinations-of-a-phone-number`](17-letter-combinations-of-a-phone-number)

**7.3 Backtracking / Trying**

- [ ] `M` [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
- [x] `M` [Word Search](https://leetcode.com/problems/word-search/) — [`79-word-search`](79-word-search)
- [ ] `H` [N Queens](https://leetcode.com/problems/n-queens/)
- [ ] `H` Rat in a Maze
- [ ] `M` M Coloring Problem
- [ ] `H` [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
- [ ] `H` [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)
- [ ] `H` [Kth Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

## Step 8 — Bit Manipulation — 1/18 matched


**8.1 Learn**

- [ ] Intro to bit manipulation
- [ ] `E` Check i-th bit set
- [ ] `E` Check odd/even
- [ ] `E` [Check power of 2](https://leetcode.com/problems/power-of-two/)
- [ ] `E` [Count set bits](https://leetcode.com/problems/number-of-1-bits/)
- [ ] `E` Set/unset rightmost unset bit
- [ ] `E` Swap two numbers (XOR)
- [ ] `M` [Divide two integers (no */%)](https://leetcode.com/problems/divide-two-integers/)

**8.2 Interview problems**

- [ ] `E` Count bits to flip A→B
- [ ] `E` [Number appearing odd times](https://leetcode.com/problems/single-number/)
- [x] `M` [Power Set (bitmask)](https://leetcode.com/problems/subsets/) — [`78-subsets`](78-subsets)
- [ ] `E` XOR of numbers L..R
- [ ] `M` [Two numbers appearing odd times](https://leetcode.com/problems/single-number-iii/)

**8.3 Advanced maths**

- [ ] `M` Print prime factors
- [ ] `M` All divisors
- [ ] `M` [Sieve of Eratosthenes](https://leetcode.com/problems/count-primes/)
- [ ] `M` Prime factorisation using sieve
- [ ] `M` Power(n, x) fast

## Step 9 — Stacks & Queues — 4/31 matched


**9.1 Learning**

- [ ] `E` Stack using arrays
- [ ] `E` Queue using arrays
- [ ] `E` [Stack using queue](https://leetcode.com/problems/implement-stack-using-queues/)
- [ ] `E` [Queue using stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
- [ ] `E` Stack using LL
- [ ] `E` Queue using LL
- [ ] `E` [Balanced parentheses](https://leetcode.com/problems/valid-parentheses/)
- [ ] `M` [Min Stack](https://leetcode.com/problems/min-stack/)

**9.2 Infix/Prefix/Postfix**

- [ ] `M` Infix → Postfix
- [ ] `M` Prefix → Infix
- [ ] `M` Prefix → Postfix
- [ ] `M` Postfix → Prefix
- [ ] `M` Postfix → Infix
- [ ] `M` Infix → Prefix

**9.3 Monotonic stack/queue**

- [ ] `E` [Next Greater Element](https://leetcode.com/problems/next-greater-element-i/)
- [ ] `M` [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
- [ ] `E` Next Smaller Element
- [ ] `M` Number of NGEs to the right
- [x] `H` [Trapping Rainwater](https://leetcode.com/problems/trapping-rain-water/) — [`42-trapping-rain-water`](42-trapping-rain-water)
- [ ] `M` [Sum of subarray minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)
- [x] `M` [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) — [`735-asteroid-collision`](735-asteroid-collision)
- [ ] `M` [Sum of subarray ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)
- [ ] `M` [Remove K Digits](https://leetcode.com/problems/remove-k-digits/)
- [ ] `H` [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- [ ] `H` [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

**9.4 Implementation**

- [x] `H` [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) — [`239-sliding-window-maximum`](239-sliding-window-maximum)
- [ ] `M` [Stock Span Problem](https://leetcode.com/problems/online-stock-span/)
- [x] `M` [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — [`1036-rotting-oranges`](1036-rotting-oranges)
- [ ] `M` The Celebrity Problem
- [ ] `M` [LRU Cache](https://leetcode.com/problems/lru-cache/)
- [ ] `H` [LFU Cache](https://leetcode.com/problems/lfu-cache/)

## Step 10 — Sliding Window & Two Pointer — 4/12 matched


**10.1 Medium**

- [x] `M` [Longest Substring w/o Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — [`3-longest-substring-without-repeating-characters`](3-longest-substring-without-repeating-characters)
- [x] `M` [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) — [`1046-max-consecutive-ones-iii`](1046-max-consecutive-ones-iii)
- [ ] `M` [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
- [x] `M` [Longest Repeating Char Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) — [`424-longest-repeating-character-replacement`](424-longest-repeating-character-replacement)
- [ ] `M` [Binary subarray with sum](https://leetcode.com/problems/binary-subarrays-with-sum/)
- [ ] `M` [Count nice subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)
- [ ] `M` [Substrings with all 3 chars](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)
- [ ] `M` [Max points from cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

**10.2 Hard**

- [ ] `M` [Longest Substring ≤ K distinct](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [ ] `H` [Subarrays with K different integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
- [x] `H` [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — [`76-minimum-window-substring`](76-minimum-window-substring)
- [ ] `H` [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)

## Step 11 — Heaps / Priority Queue — 5/17 matched


**11.1 Learning**

- [ ] PQ / Binary Heap intro
- [ ] `M` Min/Max Heap implementation

**11.2 Medium**

- [ ] `E` Check array is min-heap
- [ ] `E` Convert min-heap to max-heap
- [ ] `M` [Kth largest in array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [ ] `M` Kth smallest in array
- [ ] `M` Sort K-sorted array
- [ ] `H` [Merge K sorted lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [ ] `E` Replace elements by rank
- [x] `M` [Task Scheduler](https://leetcode.com/problems/task-scheduler/) — [`621-task-scheduler`](621-task-scheduler)
- [x] `M` [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) — [`876-hand-of-straights`](876-hand-of-straights)

**11.3 Hard**

- [x] `M` [Design Twitter](https://leetcode.com/problems/design-twitter/) — [`355-design-twitter`](355-design-twitter)
- [ ] `M` Connect ropes with min cost
- [ ] `E` [Kth largest in a stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [ ] `M` Maximum Sum Combination
- [x] `H` [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) — [`295-find-median-from-data-stream`](295-find-median-from-data-stream)
- [x] `M` [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) — [`347-top-k-frequent-elements`](347-top-k-frequent-elements)

## Step 12 — Greedy Algorithms — 1/16 matched


**12.1 Easy**

- [ ] `E` [Assign Cookies](https://leetcode.com/problems/assign-cookies/)
- [ ] `M` Fractional Knapsack
- [ ] `E` Minimum coins (greedy)
- [ ] `E` [Lemonade Change](https://leetcode.com/problems/lemonade-change/)
- [ ] `M` [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)

**12.2 Medium/Hard**

- [ ] `E` N meetings in one room
- [ ] `M` [Jump Game](https://leetcode.com/problems/jump-game/)
- [ ] `M` [Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [ ] `M` Minimum Platforms
- [ ] `M` Job Sequencing
- [ ] `H` [Candy](https://leetcode.com/problems/candy/)
- [ ] `E` SJF scheduling
- [ ] `M` LRU page replacement
- [ ] `M` [Insert Interval](https://leetcode.com/problems/insert-interval/)
- [x] `M` [Merge Intervals](https://leetcode.com/problems/merge-intervals/) — [`56-merge-intervals`](56-merge-intervals)
- [ ] `M` [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

## Step 13 — Binary Trees — 6/36 matched


**13.1 Traversals**

- [ ] Intro to trees / representation
- [ ] `E` [Preorder](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [ ] `E` [Inorder](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [ ] `E` [Postorder](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [ ] `M` [Level order](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [ ] `E` Iterative Preorder
- [ ] `E` Iterative Inorder
- [ ] `E` Iterative Postorder (2 stacks)
- [ ] `M` Iterative Postorder (1 stack)
- [ ] `M` All traversals in one pass

**13.2 Medium**

- [ ] `E` [Height of BT](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] `E` [Balanced BT](https://leetcode.com/problems/balanced-binary-tree/)
- [x] `E` [Diameter of BT](https://leetcode.com/problems/diameter-of-binary-tree/) — [`543-diameter-of-binary-tree`](543-diameter-of-binary-tree)
- [x] `H` [Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — [`124-binary-tree-maximum-path-sum`](124-binary-tree-maximum-path-sum)
- [ ] `E` [Identical Trees](https://leetcode.com/problems/same-tree/)
- [ ] `M` [Zig-Zag Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
- [ ] `M` Boundary Traversal
- [x] `H` [Vertical Order Traversal](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) — [`1029-vertical-order-traversal-of-a-binary-tree`](1029-vertical-order-traversal-of-a-binary-tree)
- [ ] `M` Top View
- [ ] `M` Bottom View
- [x] `M` [Right/Left View](https://leetcode.com/problems/binary-tree-right-side-view/) — [`199-binary-tree-right-side-view`](199-binary-tree-right-side-view)
- [ ] `E` [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

**13.3 Hard**

- [ ] `M` Root to node path
- [x] `M` [LCA in BT](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) — [`236-lowest-common-ancestor-of-a-binary-tree`](236-lowest-common-ancestor-of-a-binary-tree)
- [ ] `M` [Max width of BT](https://leetcode.com/problems/maximum-width-of-binary-tree/)
- [ ] `M` Children Sum Property
- [x] `M` [All nodes distance K](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) — [`893-all-nodes-distance-k-in-binary-tree`](893-all-nodes-distance-k-in-binary-tree)
- [ ] `H` Min time to burn tree
- [ ] `E` [Count nodes in complete BT](https://leetcode.com/problems/count-complete-tree-nodes/)
- [ ] `M` Requirements to construct unique BT
- [ ] `M` [Construct BT from Preorder+Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [ ] `M` [Construct BT from Postorder+Inorder](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
- [ ] `H` [Serialize & Deserialize BT](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [ ] `M` Morris Preorder
- [ ] `M` Morris Inorder
- [ ] `M` [Flatten BT to LL](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Step 14 — Binary Search Trees — 0/16 matched


**14.1 Concepts**

- [ ] Intro to BST
- [ ] `E` [Search in BST](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [ ] `E` Min/Max in BST

**14.2 Practice**

- [ ] `E` Ceil in BST
- [ ] `E` Floor in BST
- [ ] `M` [Insert node in BST](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- [ ] `M` [Delete node in BST](https://leetcode.com/problems/delete-node-in-a-bst/)
- [ ] `M` [Kth smallest/largest in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- [ ] `M` [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/)
- [ ] `M` [LCA in BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [ ] `M` [Construct BST from preorder](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)
- [ ] `M` Inorder Successor/Predecessor
- [ ] `H` Merge two BSTs
- [ ] `E` [Two Sum in BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)
- [ ] `M` [Recover BST](https://leetcode.com/problems/recover-binary-search-tree/)
- [ ] `H` Largest BST in BT

## Step 15 — Graphs — 10/48 matched


**15.1 Learning**

- [ ] Graph & types
- [ ] Representation
- [ ] `M` Connected components
- [ ] `M` [BFS](https://leetcode.com/problems/breadth-first-search/)
- [ ] `M` DFS

**15.2 BFS/DFS problems**

- [ ] `M` [Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- [ ] `M` [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [x] `M` [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — [`1036-rotting-oranges`](1036-rotting-oranges)
- [ ] `E` [Flood Fill](https://leetcode.com/problems/flood-fill/)
- [ ] `M` Cycle detection undirected (BFS)
- [ ] `M` Cycle detection undirected (DFS)
- [ ] `M` [0/1 Matrix (nearest cell)](https://leetcode.com/problems/01-matrix/)
- [x] `M` [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) — [`130-surrounded-regions`](130-surrounded-regions)
- [ ] `M` [Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/)
- [x] `H` [Word Ladder I](https://leetcode.com/problems/word-ladder/) — [`127-word-ladder`](127-word-ladder)
- [ ] `H` [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)
- [ ] `M` Number of Distinct Islands
- [x] `M` [Bipartite Graph](https://leetcode.com/problems/is-graph-bipartite/) — [`801-is-graph-bipartite`](801-is-graph-bipartite)
- [ ] `M` Cycle detection directed (DFS)

**15.3 Topo sort**

- [ ] `M` Topo Sort (DFS)
- [ ] `M` Kahn's Algorithm (BFS)
- [ ] `M` Cycle detection directed (BFS)
- [x] `M` [Course Schedule I](https://leetcode.com/problems/course-schedule/) — [`207-course-schedule`](207-course-schedule)
- [ ] `M` [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [ ] `M` [Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)
- [ ] `H` [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

**15.4 Shortest path**

- [ ] `M` Shortest path UG unit weights
- [ ] `M` Shortest path in DAG
- [x] `M` [Dijkstra's Algorithm](https://leetcode.com/problems/network-delay-time/) — [`744-network-delay-time`](744-network-delay-time)
- [ ] `M` [Shortest path in binary maze](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
- [ ] `M` [Path with Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
- [x] `M` [Cheapest Flights within K stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) — [`803-cheapest-flights-within-k-stops`](803-cheapest-flights-within-k-stops)
- [ ] `M` [Number of ways to arrive at destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)
- [ ] `H` Bellman Ford
- [ ] `H` Floyd Warshall
- [ ] `M` [City with smallest #neighbors](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

**15.5 MST / Disjoint Set**

- [ ] MST theory
- [x] `M` [Prim's Algorithm](https://leetcode.com/problems/min-cost-to-connect-all-points/) — [`1706-min-cost-to-connect-all-points`](1706-min-cost-to-connect-all-points)
- [ ] `M` Disjoint Set (union by rank/size)
- [ ] `M` Kruskal's Algorithm
- [ ] `M` [Operations to make network connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)
- [ ] `M` [Most Stones Removed](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)
- [x] `M` [Accounts Merge](https://leetcode.com/problems/accounts-merge/) — [`721-accounts-merge`](721-accounts-merge)
- [x] `H` [Making a Large Island](https://leetcode.com/problems/making-a-large-island/) — [`854-making-a-large-island`](854-making-a-large-island)
- [ ] `H` [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

**15.6 Advanced**

- [ ] `H` [Bridges in graph](https://leetcode.com/problems/critical-connections-in-a-network/)
- [ ] `H` Articulation Point
- [ ] `H` Kosaraju's Algorithm (SCC)

## Step 16 — Dynamic Programming — 14/55 matched


**16.1 Intro**

- [ ] DP introduction / memo vs tab

**16.2 1D DP**

- [x] `E` [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) — [`70-climbing-stairs`](70-climbing-stairs)
- [ ] `M` Frog Jump
- [ ] `M` Frog Jump k distances
- [x] `M` [House Robber](https://leetcode.com/problems/house-robber/) — [`198-house-robber`](198-house-robber)
- [x] `M` [House Robber II](https://leetcode.com/problems/house-robber-ii/) — [`213-house-robber-ii`](213-house-robber-ii)

**16.3 2D/Grid DP**

- [ ] `M` Ninja's Training
- [x] `M` [Unique Paths](https://leetcode.com/problems/unique-paths/) — [`62-unique-paths`](62-unique-paths)
- [ ] `M` [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
- [ ] `M` [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- [ ] `M` [Triangle](https://leetcode.com/problems/triangle/)
- [ ] `M` [Min/Max Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)
- [ ] `H` [Cherry Pickup II (3D)](https://leetcode.com/problems/cherry-pickup-ii/)

**16.4 DP on subsequences**

- [ ] `M` Subset sum equal to target
- [x] `M` [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — [`416-partition-equal-subset-sum`](416-partition-equal-subset-sum)
- [ ] `H` Partition min abs sum diff
- [ ] `M` Count subsets with sum K
- [ ] `M` Count partitions with given diff
- [ ] `M` 0/1 Knapsack
- [x] `M` [Minimum Coins](https://leetcode.com/problems/coin-change/) — [`322-coin-change`](322-coin-change)
- [x] `M` [Target Sum](https://leetcode.com/problems/target-sum/) — [`494-target-sum`](494-target-sum)
- [x] `M` [Coin Change 2](https://leetcode.com/problems/coin-change-ii/) — [`518-coin-change-ii`](518-coin-change-ii)
- [ ] `M` Unbounded Knapsack
- [ ] `M` Rod Cutting

**16.5 DP on strings**

- [x] `M` [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) — [`1250-longest-common-subsequence`](1250-longest-common-subsequence)
- [ ] `M` Print LCS
- [ ] `M` Longest Common Substring
- [ ] `M` [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- [ ] `H` [Min insertions to make palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)
- [ ] `M` [Min insert/delete A→B](https://leetcode.com/problems/delete-operation-for-two-strings/)
- [ ] `H` [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)
- [x] `H` [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) — [`115-distinct-subsequences`](115-distinct-subsequences)
- [x] `M` [Edit Distance](https://leetcode.com/problems/edit-distance/) — [`72-edit-distance`](72-edit-distance)
- [ ] `H` [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

**16.6 DP on stocks**

- [ ] `E` [Best Time to Buy/Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [ ] `M` [Buy/Sell II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [ ] `H` [Buy/Sell III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
- [ ] `H` [Buy/Sell IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
- [x] `M` [Buy/Sell with cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) — [`309-best-time-to-buy-and-sell-stock-with-cooldown`](309-best-time-to-buy-and-sell-stock-with-cooldown)
- [ ] `M` [Buy/Sell with fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

**16.7 DP on LIS**

- [x] `M` [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) — [`300-longest-increasing-subsequence`](300-longest-increasing-subsequence)
- [ ] `M` Print LIS
- [ ] `M` LIS binary search
- [ ] `M` [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/)
- [ ] `M` [Longest String Chain](https://leetcode.com/problems/longest-string-chain/)
- [ ] `M` Longest Bitonic Subsequence
- [ ] `M` [Number of LIS](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

**16.8 Partition / MCM DP**

- [ ] `H` Matrix Chain Multiplication
- [ ] `H` [Min Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)
- [x] `H` [Burst Balloons](https://leetcode.com/problems/burst-balloons/) — [`312-burst-balloons`](312-burst-balloons)
- [ ] `H` Boolean Evaluation to True
- [ ] `H` [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)
- [ ] `M` [Partition Array for Max Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/)

**16.9 DP on squares**

- [ ] `M` [Count Square Submatrices with all 1s](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
- [ ] `H` [Maximal Rectangle of 1s](https://leetcode.com/problems/maximal-rectangle/)

## Step 17 — Tries — 0/7 matched


**17.1 Theory**

- [ ] `M` [Implement Trie (insert/search/startsWith)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [ ] `M` [Implement Trie II (count)](https://leetcode.com/problems/implement-trie-ii-prefix-tree/)

**17.2 Problems**

- [ ] `M` [Longest word with all prefixes](https://leetcode.com/problems/longest-word-in-dictionary/)
- [ ] `H` Number of distinct substrings
- [ ] Bit prereq for trie (theory)
- [ ] `M` [Maximum XOR of two numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
- [ ] `H` [Maximum XOR with element from array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

## Step 18 — Strings [Hard] — 0/9 matched


**18.1 Hard string problems**

- [ ] `M` Min bracket reversals
- [ ] `M` [Count and Say](https://leetcode.com/problems/count-and-say/)
- [ ] String hashing (theory)
- [ ] `H` Rabin-Karp
- [ ] `H` Z-Function
- [ ] `H` [KMP / LPS array](https://leetcode.com/problems/shortest-palindrome/)
- [ ] `H` [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)
- [ ] `H` [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/)
- [ ] `H` [Count palindromic subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/)
