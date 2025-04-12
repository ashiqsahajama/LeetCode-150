# LeetCode 909: Snakes and Ladders

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/snakes-and-ladders/)

You are given an `n x n` integer matrix `board` representing the game board. Each cell contains:
- `-1` for a normal square,
- A positive number indicating a snake or ladder jump to another square.

The board is numbered from `1` to `n*n` in a Boustrophedon style (left-to-right, right-to-left alternation per row from bottom to top). You start at square `1` and can move from `1` to `6` squares on each turn. Return the **minimum number of moves** to reach square `n*n`, or `-1` if it's not possible.

### Constraints:
1. `2 <= board.length == board[i].length <= 20`
2. `board[i][j]` is either `-1` or a value from `1` to `n*n`
3. The destination of a snake or ladder is always different from its start.

### Examples:

| Input | Output | Explanation |
|-------|--------|-------------|
| `[[ -1, -1, -1, -1, -1, -1 ], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [ -1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1 ]]` | `4` | Uses ladders at `2 → 15`, `5 → 35`, and `9 → 13` to reach the goal in 4 moves. |

---

## Solution Explanation

This solution uses **Breadth-First Search (BFS)** to find the shortest path from square `1` to square `n*n`:

1. **Reverse the board**:
   - Since the numbering starts from the bottom row, reverse the board to align index calculations.

2. **Convert Position to Coordinates**:
   - Define `getpos(pos)` to convert 1D position to 2D indices `(r, c)` considering Boustrophedon layout.

3. **BFS Traversal**:
   - Start from position `1`, with `0` moves.
   - For each position, simulate a die roll (`+1` to `+6`).
   - If the destination has a ladder/snake (`board[r][c] != -1`), jump to the specified square.
   - Track visited positions to avoid cycles.
   - If we reach `n*n`, return the number of moves.

4. **Edge Case**:
   - If we exhaust the queue without reaching the end, return `-1`.

---

## Code

```python
from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def getpos(pos):
            r = (pos - 1) // length
            c = (pos - 1) % length
            if r % 2:
                c = length - c - 1
            return [r, c]

        queue = deque()
        visited = set()
        queue.append([1, 0])
        visited.add(1)

        while queue:
            curr, moves = queue.popleft()

            for val in range(1, 7):
                nextstep = curr + val
                if nextstep > length * length:
                    continue
                r, c = getpos(nextstep)
                if board[r][c] != -1:
                    nextstep = board[r][c]
                if nextstep == length * length:
                    return moves + 1
                if nextstep not in visited:
                    visited.add(nextstep)
                    queue.append([nextstep, moves + 1])
        return -1
