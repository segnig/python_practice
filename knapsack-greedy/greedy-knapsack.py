# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:30:30 2024

@author: segni
"""

class Food(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.calories = weight
        self.value = value
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()
    
    def __str__(self):
        return self.name + ": < " + str(self.value) + ",  " + str(self.calories) + '>'
    
    
def buildMenu(names, values, calories):
    """
    name, values, calories lists of the same 
    length name a list of strings values and 
    calories lists of numbers return list of Foods
    
    """
    menu = []
    
    
    
    for i in range(len(values)):
        food = Food(names[i], values[i], calories[i])
        menu.append(food)
                    
    return menu


def greedy(items, maxCost, keyFunction):
    """
    Assume items a list , maxCost >= 0 
    keyFunction maps elements of items to numbers
    """
    
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0 
    
    for i in range(len(itemsCopy)):
        if totalCost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy)
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
            
    return result, totalValue


def testGreedy(items, constraints, keyFunction):
    taken, val = greedy(items, constraints, keyFunction)
    
    print(f"Total vales of items taken = {val}")
    for item in items:
        print("   ", item)
    

def testGreedys(foods, maxUnits):
    print("Use greedy by values to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    
    print("Use greedy by cost to allocate", maxUnits, "calories")
    
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print("Use greedy by density to allocate", maxUnits, "calories")
    
    testGreedy(foods, maxUnits, Food.density)
        
names = ["wine", "beer", "pizza", "burger", "fries",
         "cola", "apple", "donut", "cake"]
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)