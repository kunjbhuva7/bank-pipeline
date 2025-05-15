from modules.card_verification import verify_card
from modules.language_selection import select_language
from modules.withdrawal import withdraw
from modules.pin_verification import verify_pin
from modules.logger import log_transaction
from modules.sms_notification import send_sms

balance = 10000

def run_transaction():
    print("🏦 Welcome to the Bank ATM\n")
    if verify_card():
        language = select_language()
        amount = withdraw(balance)
        if amount == 0:
            print("Transaction cancelled due to insufficient funds.")
            return
        if verify_pin():
            global balance
            balance -= amount
            print(f"\n✅ Withdrawal successful: ₹{amount}")
            print(f"💰 Remaining balance: ₹{balance}")

            # Log transaction
            log_transaction("Withdrawal", amount, balance)
            
            # Send SMS notification
            send_sms(amount, balance)
        else:
            print("❌ Invalid PIN. Transaction aborted.")
            log_transaction("Failed PIN", 0, balance)
    else:
        print("❌ Card verification failed.")
        log_transaction("Card Verification Failed", 0, balance)

if __name__ == "__main__":
    run_transaction()

