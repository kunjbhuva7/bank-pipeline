import os
from datetime import datetime

def send_sms(amount=11350, balance=45000):
    try:
        from twilio.rest import Client

        # Environment variables se credentials uthao
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_FROM_NUMBER")
        to_number = os.getenv("TO_PHONE_NUMBER")

        # Agar credentials set nahi hain, to SMS bhejna skip karo
        if not all([account_sid, auth_token, from_number, to_number]):
            print("⚠️ SMS credentials not set. Skipping SMS sending.")
            return

        # Customize transaction details
        account_number = "XXXXXX870432"
        bank_name = "Team IDFC FIRST Bank"
        helpline = "180010888"
        date_str = datetime.now().strftime("%d/%m/%y %H:%M")

        # SMS ka message body
        message_body = (
            f"Dear Customer, your A/C {account_number} is debited by INR {amount:.2f} "
            f"on {date_str}. New Bal: INR {balance:,.2f}. "
            f"For dispute, call {helpline}. - {bank_name}"
        )

        # Twilio client initialize karo
        client = Client(account_sid, auth_token)

        # SMS bhejo
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )

        # Console me success message print karo
        print(f"✅ SMS sent successfully. SID: {message.sid}")
        print(f"📩 Message: {message_body}")

    except ImportError:
        print("❌ Twilio module not installed. Please run 'pip install twilio' to enable SMS notifications.")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")

# Agar script direct run ho rahi hai to SMS bhejo
if __name__ == "__main__":
    print("🚀 Triggering SMS notification from CI/CD pipeline...")
    send_sms()

