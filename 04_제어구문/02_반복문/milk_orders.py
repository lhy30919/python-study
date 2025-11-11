milk_orders = {
    '101': {'milk': 1, 'yogurt': 5},
    '102': {'milk': 2},
    '103': {'milk': 1, 'yogurt': 10},
    '104': {'yogurt': 15}
}

for room, orders in milk_orders.items():
    print(f"{room}호 주문 내역:")
    for item, count in orders.items():
        print(f"  - {item}: {count}개")
    print()
