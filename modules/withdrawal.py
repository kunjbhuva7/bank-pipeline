def withdraw(balance):
    try:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be positive.")
            return 0
        if amount > balance:
            print("Insufficient Balance! ❌")
            return 0
        return amount
    except ValueError:
        print("Invalid amount entered.")
        return 0

