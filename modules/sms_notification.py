import os

def send_sms(amount=1000, balance=5000):
    try:
        from twilio.rest import Client

        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_FROM_NUMBER")
        to_number = os.getenv("TO_PHONE_NUMBER")

        if not all([account_sid, auth_token, from_number, to_number]):
            print("⚠️ SMS credentials not set. Skipping SMS sending.")
            return

        client = Client(account_sid, auth_token)
        message_body = f"📲 Your account has been debited by ₹{amount}. Available balance: ₹{balance}. Thank you for banking with us."

        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )

        print(f"✅ SMS sent successfully. SID: {message.sid}")
    except ImportError:
        print("❌ Twilio module not installed. Please run 'pip install twilio' to enable SMS notifications.")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")

# Run this block when called from CI/CD
if __name__ == "__main__":
    print("🚀 Triggering SMS notification from CI/CD pipeline...")
    send_sms()

