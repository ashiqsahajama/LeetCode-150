# LeetCode 150 Solutions

## Table of Contents
- [Insert Delete GetRandom O(1)](LeetCode/InsertDeleteGetRandomO1)

---

## Problem Explanations

### Insert Delete GetRandom O(1)

- **Problem:** [LeetCode Link](https://leetcode.com/problems/insert-delete-getrandom-o1/)

  Implement the `RandomizedSet` class:

  - `RandomizedSet()` Initializes the RandomizedSet object.
  - `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
  - `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
  - `int getRandom()` Returns a random element from the current set of elements. Each element must have the same probability of being returned.

  You must implement the functions in **O(1)** time complexity.

---

### Solution Explanation

This solution uses two data structures:
1. **List (`obj`)**: To store the elements of the set for O(1) access to a random element.
2. **Dictionary (`dict`)**: To store the mapping of values to their indices in the list for O(1) lookup, insertion, and deletion.

#### Key Operations:
1. **Insert**:
   - Check if the value exists in the dictionary (`dict`). If it does, return `False`.
   - Otherwise, append the value to the list (`obj`) and store its index in the dictionary (`dict`).
   - Time complexity: O(1).

2. **Remove**:
   - Check if the value exists in the dictionary. If it doesn't, return `False`.
   - Otherwise:
     - Swap the value to be removed with the last element in the list.
     - Update the dictionary for the swapped value.
     - Remove the last element from the list and delete the value from the dictionary.
   - Time complexity: O(1).

3. **GetRandom**:
   - Use Python's `random.choice` function to select a random element from the list.
   - Time complexity: O(1).

