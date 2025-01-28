# LeetCode 71: Simplify Path

## Table of Contents
- [Problem Explanation](#problem-explanation)
- [Solution Explanation](#solution-explanation)
- [Code](#code)
- [How to Run](#how-to-run)
- [Complexity Analysis](#complexity-analysis)

---

## Problem Explanation

- **Problem Link**: [LeetCode Problem](https://leetcode.com/problems/simplify-path/)

Given a string `path`, which is an **absolute path** (starting with a `/`) to a file or directory in a Unix-style file system, simplify it. The simplified canonical path should have the following format:
1. The path starts with a single `/`.
2. Any two directories are separated by a single `/`.
3. The path does not end with a trailing `/`.
4. The path only contains the directories on the path from the root directory to the target file or directory (i.e., no `.` or `..`).

Return the simplified canonical path.

### Constraints:
1. \( 1 \leq \text{path.length} \leq 3000 \)
2. `path` consists of English letters, digits, period (`.`), slash (`/`), or an underscore (`_`).
3. `path` is a valid absolute Unix path.

### Examples:

| Input                     | Output        |
|---------------------------|---------------|
| `path = "/home/"`         | `"/home"`     |
| `path = "/../"`           | `"/"`         |
| `path = "/home//foo/"`    | `"/home/foo"` |

---

## Solution Explanation

This solution simplifies the Unix-style file path using a **stack-based approach**:

### Steps:

1. **Split the Path**:
   - Split the input string `path` into components using the `/` character.
   - This gives a list of path elements.

2. **Initialize a Stack**:
   - Use a stack to keep track of the valid directories.

3. **Iterate Through Path Components**:
   - Skip empty strings and `"."` (current directory).
   - If the component is `".."` (parent directory), pop the last directory from the stack (if the stack is not empty).
   - Otherwise, push valid directory names onto the stack.

4. **Build the Simplified Path**:
   - Join the stack elements with `/` and prepend a leading `/`.

5. **Return the Result**:
   - Return the canonical path as a string.

---

## Code

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        items = path.split("/")  # Split path into components

        for i in items:
            if i == "..":  # Go up a directory
                if stack:
                    stack.pop()
            elif i != "" and i != ".":  # Valid directory name
                stack.append(i)
        
        # Join stack into a simplified path
        return "/" + "/".join(stack)
