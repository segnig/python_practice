## Knapsack Problem Solver

This program implements a greedy algorithm to solve the knapsack problem in the context of choosing the most valuable food options under a calorie constraint.

**Problem:**

Given a set of food items, each with a value (e.g., monetary) and a weight (represented by calories), and a maximum weight capacity (represented by maximum calories), the goal is to find the subset of items that provides the highest total value without exceeding the weight limit.

I'd be glad to create a comprehensive README file for your GitHub repository that clearly defines the problem, explains the code, and provides usage instructions:

**Food Value Optimization**

This Python program addresses the **0/1 Knapsack Problem** in the context of selecting food items with the highest total value within a calorie constraint.

**Problem Definition:**

The knapsack problem is a classic optimization problem where you have a limited capacity (knapsack) and a set of items with weights and values. The goal is to select a subset of items that maximizes the total value you can carry without exceeding the capacity.

In this program, the knapsack represents a fixed calorie limit, and the items are food items with values and calorie costs. We aim to find the combination of food items that provides the highest total value while staying within the calorie limit.

**Code Breakdown:**

**Classes:**

- `Food`: Represents a food item with its name, value, and calorie cost.

**Functions:**

- `buildMenu(names, values, calories)`: Creates a list of `Food` objects from provided names, values, and calorie lists.
- `greedy(items, maxCost, keyFunction)`: Implements a greedy algorithm that prioritizes items based on the `keyFunction` (value, inverse cost, or density) until the calorie constraint (`maxCost`) is reached. It returns the selected items and their total value.
- `testGreedy(items, constraints, keyFunction)`: Tests the `greedy` function with specified items, constraint (calorie limit), and key function, printing the total value and details of selected items.
- `testGreedys(foods, maxUnits)`: Runs the `testGreedy` function with different key functions (value, inverse cost, and density) for a given food menu and calorie limit.
- `maxVal(toConsider, avail)`: Implements a backtracking solution for the 0/1 knapsack problem. It recursively explores all possible combinations of items and returns the combination with the maximum total value within the calorie constraint (`avail`).
- `fastMaxVal(toConsider, avail, memo={})`: Implements a dynamic programming solution for the 0/1 knapsack problem. It recursively explores all possible combinations of items and returns the combination with the maximum total value within the calorie constraint (`avail`). `memo` default empty dictionary.
- `testMaxVal(foods, maxUnits, algorithm, printItems=True)`: Tests the `maxVal or fastMaxVal` based on the `algorithm` parameter function with a food menu, calorie limit, and optional flag to print the details of selected items.

**Usage:**

1. **Save the code:** Save the code as a Python file (e.g., `greedy-knapsack.py`).
2. **Run the program:** Execute the script from the command line using `python greedy-knapsack.py`.

**Output:**

The program displays the results of the greedy algorithms for different prioritization criteria and the optimal solution obtained through the knapsack search tree.

**Example:**

```
Use greedy by values to allocate 750 calories
Total vales of items taken = 284
     burger: < 100,  354>
     pizza: < 95,  258>
     wine: < 89,  123>
Use greedy by cost to allocate 750 calories
Total vales of items taken = 320
     apple: < 50,  95>
     wine: < 89,  123>
     cake: < 12,  123>
     cola: < 79,  150>
     beer: < 90,  154>
Use greedy by density to allocate 750 calories
Total vales of items taken = 320
     wine: < 89,  123>
     beer: < 90,  154>
     cola: < 79,  150>
     apple: < 50,  95>
     cake: < 12,  123>
************
Use search tree to allocate 750 calories
Total value of items taken = 353
     cola: < 79,  150>
     pizza: < 95,  258>
     beer: < 90,  154>
     wine: < 89,  123>
```

**Further Enhancements:**

- Allow user input for food items, values, and calorie constraints.
- Explore other optimization algorithms for larger datasets.
- Visualize the results using libraries like Matplotlib.


I hope this README file provides a clear and informative guide to the program's functionality!
