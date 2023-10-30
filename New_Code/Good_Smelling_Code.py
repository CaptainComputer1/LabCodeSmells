def calculate_total_price_new(items):
    items = filter(lambda item: item.quantity > 0, items)
    total = 0
    for item in items:
        discount = 0.9 if item.price > 100 else 0.95
        total += item.price * discount
    return total