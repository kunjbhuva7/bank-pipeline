def verify_pin():
    pin = input("Enter your 4-digit PIN: ")
    if pin == "1234":
        print("PIN verified ✅")
        return True
    else:
        print("Incorrect PIN ❌")
        return False

