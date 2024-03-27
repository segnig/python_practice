
class Food(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.calories = calories
        self.value = value
        
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()
    
    
    def __str__(self):
        return self.name + ": < " + str(self.value) + ",  " + str(self.calories) + '>'
    
    
def buildMenu(names:list, values:list, calories:list):
    menu = []
    for i in range(len(names)):
        food = Food(names[i], values[i], calories[i])
        menu.append(food)
    return menu

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0, 0.0
    
    for i in range(len(itemsCopy)):
        if totalCost + itemsCopy[i].getCost() <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
            
    return result, totalValue


def testGreedy(items, constraints, keyFunction):
    taken, val = greedy(items, constraints, keyFunction)
    
    print(f"Total vales of items taken = {val}")
    for item in items:
        print("    ", item)
    

def testGreedys(foods, maxUnits):
    print("Use greedy by values to allocate", maxUnits, "calories")
    testGreedy(foods, maxUnits, Food.getValue)
    
    print("Use greedy by cost to allocate", maxUnits, "calories")
    
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))
    
    print("Use greedy by density to allocate", maxUnits, "calories")
    
    testGreedy(foods, maxUnits, Food.density)

def maxVal(toConsider, avail):
    """
    Assume toCosider a list of items, avail a weight 
    Return  a tuple of the total value of a solution 
    to the 0/1 knapsack problem and the items of that solution
    """
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
        
    else:
        nextItem = toConsider[0]
        # Explore left branch 
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        
        withVal += nextItem.getValue()
        # Exploree right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
        
    return result

def testMaxVal(foods, maxUnits, printItems=True):
    print("Use search tree to allocate", maxUnits, "calories")
    
    val, taken = maxVal(foods, maxUnits)
    print("Total value of items taken =", val)
    if printItems:
        for item in taken:
            print ("    ", item)

if __name__ == "__main__":      
    names = ["wine", "beer", "pizza", "burger", "fries",
            "cola", "apple", "donut", "cake"]
    values = [89, 90, 95, 100, 90, 79, 50, 10, 12]
    calories = [123, 154, 258, 354, 365, 150, 95, 195, 123]
    foods = buildMenu(names, values, calories)
    testGreedys(foods, 750)
    print("************")
    testMaxVal(foods, 750)
        
