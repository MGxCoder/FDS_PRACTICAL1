bal = 5000

while True:
    print("Enter transactions in the format: D[amount] or W[amount]")
    trans = input()
    trans = trans.split()  
    if not trans:  
        break
    elif trans[0] == "D":
        bal = bal + int(trans[1])
    elif trans[0] == "W":
        if bal < int(trans[1]):
            print("Insufficient Balance")
        else:
            bal = bal - int(trans[1])

    print("Balance:", bal)
