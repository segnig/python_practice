## Knapsack Problem Solver

This program implements a greedy algorithm to solve the knapsack problem in the context of choosing the most valuable food options under a calorie constraint.

**Problem:**

Given a set of food items, each with a value (e.g., monetary) and a weight (represented by calories), and a maximum weight capacity (represented by maximum calories), the goal is to find the subset of items that provides the highest total value without exceeding the weight limit.

**Solution:**

This program utilizes a greedy approach. It first builds a menu of food items using the `buildMenu` function. Then, the `testGreedys` function demonstrates the `greedy` algorithm, which iteratively selects items with the highest value per unit weight (density) or other sorting criteria until the calorie constraint is reached.

**Usage:**

1.  **No modifications required to run the code.** The script defines sample food items and demonstrates using the greedy algorithm with different sorting criteria.
2.  **Change food data (optional):** You can modify the `names`, `values`, and `calories` lists to define your own set of food items.
3.  **Adjust constraint (optional):** The `testGreedys` function sets the maximum calorie constraint (`maxUnits`). Change this value to adjust the calorie limit for your scenario.

**Output:**

The program prints the results of using the greedy algorithm with three sorting approaches:

* **Value:** Sorts by highest value first.
* **Cost (Inverse Density):** Sorts by lowest calorie cost first (achieved by inverting density).
* **Density:** Sorts by value per calorie (highest density first).

This allows you to compare which approach yields the most valuable food combination within the specified calorie restriction.

**Dependencies:**

The code requires no external libraries beyond Python's built-in functionalities.
