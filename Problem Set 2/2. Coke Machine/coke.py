print("Amount Due: 50")

due_amount=50
added_coins=0

while True:

    insertcoin=int (input("Insert Coin: "))

    if insertcoin==25 or insertcoin==10 or insertcoin==5:
        due_amount-=insertcoin
        added_coins+=insertcoin

    if added_coins>=50:
        print(f"Owed Change: {added_coins-50}")
        break
    else:
        print(f"Due Amount: {due_amount}")