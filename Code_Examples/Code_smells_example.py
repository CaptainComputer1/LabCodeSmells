#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            if item.price > 100:
                total += item.price * 0.9
            else:
                total += item.price * 0.95
    return total

def calculate_total_price_new(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            discount = 0.9 if item.price > 100 else 0.95
            total += item.price * discount
    return total