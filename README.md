# advent-2025
yet another advent of code 2025 repository.

## solution sketches
1. Simulation + checking for zero-crossings. There are lots of edge cases in Part 2, and moves that do several full rotations need to be considered.
2. The input is small enough to brute force contents of all ranges and perform regex matching.
3. DP on pointer index inside the bank + number of batteries that still need to be picked. (I later learned this can be solved much more easily with greedy algorithm).
4. Direct implementation.
5. **(Part 1)** Brute-force checking of each ingredient against all ranges. **(Part 2)** Range merging, after sorting by range starts.
6. Direct implementation. We need to be careful of iteration orders as we move through the input.
7. DP on beam position. **(Part 1)** Count the number of activated splitters. **(Part 2)** Count the number of paths, where leaf nodes are beams that have left the grid.
8. Precompute all edges. Build DSU, merging + keeping track of number of components.
9. **(Part 1)** Brute force search. **(Part 2)** Evil checking to ensure no line intersects candidate rectangle + the next point from the candidate start point is in the proper direction (since we can determine the shape is clockwise).
10. **(Part 1)** DP on indicator states, running BFS to find shortest path to target state. **(Part 2)** Integer linear programming optimization to determine minimum number of presses such that sum of activations is required joltage.
11. **(Part 1)** DP path counting. **(Part 2)** DP path counting, with flags marking if `fft` and `dac` have been reached.
12. Check if we can naively pack each shape in a distinct 3x3 cell, which somehow works.
