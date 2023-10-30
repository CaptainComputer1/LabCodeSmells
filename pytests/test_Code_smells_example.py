import time

from Old_Code.Code_smells_example import calculate_total_price
from New_Code.Good_Smelling_Code import calculate_total_price_new
from New_Classes.Item import Item
from Tools.cognitive_complexity import get_cognitive_complexity
from tabulate import tabulate
def test_calculate_total_price():
    items = [Item("iPhone", 1, 1100.00),
             Item("Pen", 18, 7.00),
             Item("Nintendo Switch", 0, 299.99),
             Item("Zelda TOTK", 0, 69.99)]
    assert calculate_total_price(items) == 996.65
    assert calculate_total_price_new(items) == 996.65
    old_total, old_details = get_cognitive_complexity(calculate_total_price)
    print("Complexity of old price function: ")
    print(tabulate(old_details, headers=["Complexity", "Node"], tablefmt="fancy_grid"))
    new_total, new_details = get_cognitive_complexity(calculate_total_price_new)
    print("Complexity of new price function: ")
    print(tabulate(new_details, headers=["Complexity", "Node"], tablefmt="fancy_grid"))

"""
The tests for cognitive complexity were inspired by source [2].
"""