def verify_card():
    card_number = input("Enter your 4-digit card number: ")
    if card_number.isdigit() and len(card_number) == 4:
        print("Card verified ✅")
        return True
    else:
        print("Invalid card number ❌")
        return False

