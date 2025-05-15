import datetime

def log_transaction(action, amount, balance):
    with open("transaction.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {action}: ₹{amount}, Remaining: ₹{balance}\n")

