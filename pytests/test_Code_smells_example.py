from New_Code.Good_Smelling_Code import calculate_total_price_new
from New_Classes.Item import Item
def test_calculate_total_price():
    items = [Item("iPhone", 1, 1100.00),
             Item("Pen", 18, 7.00),
             Item("Nintendo Switch", 0, 299.99),
             Item("Zelda TOTK", 0, 69.99)]
    assert calculate_total_price_new(items) == 996.65