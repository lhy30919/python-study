coffee = 5
milk = 4
water = 3

coffee_price = 500
milk_price=400
water_price=300

money=0

while True:
    print(f"{'메뉴) 수량':=^20}\n\
1) {'coffee':<6}{'=':>3} {coffee}\n2) {'milk':<6}{'=':>3} {milk}\n3) {'water':<6}{'=':>3} {water}\n\
4) 잔액 반환\n\
{'가격':=^20}\n\
coffee_price = {coffee_price}\nmilk_price={water_price}\nwater_price={water_price}\n\
{'잔액':=^20}\n\
{money}\n")

    kind = input("종류를 입력하세요: ")
    money += int(input("돈을 넣어 주세요: "))

    # 커피 선택
    if kind == "1":
        if coffee == 0:
            print("커피가 모두 소진되었습니다.\n")
            continue
        if money >= coffee_price:
            money -= coffee_price
            coffee -= 1
            print("[ OUTPUT ] coffee 나왔습니다!\n")
        else:
            print("잔액이 부족합니다.\n")

    # 우유 선택
    elif kind == "2":
        if milk == 0:
            print("우유가 모두 소진되었습니다.\n")
            continue
        if money >= milk_price:
            money -= milk_price
            milk -= 1
            print("[ OUTPUT ] milk 나왔습니다!\n")
        else:
            print("잔액이 부족합니다.\n")

    # 물 선택
    elif kind == "3":
        if water == 0:
            print("물이 모두 소진되었습니다.\n")
            continue
        if money >= water_price:
            money -= water_price
            water -= 1
            print("[ OUTPUT ] water 나왔습니다!\n")
        else:
            print("잔액이 부족합니다.\n")
    elif kind == "4":
        print(f"잔액{money}원을 반환합니다.\n")
        money = 0
    else : "종류와 수량을 다시 확인하세요"


