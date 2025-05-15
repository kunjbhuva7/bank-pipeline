import os
import json
import requests
from datetime import datetime

def send_sms(amount=11350, balance=45000):
    try:
        from twilio.rest import Client

        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_FROM_NUMBER")
        to_number = os.getenv("TO_PHONE_NUMBER")

        if not all([account_sid, auth_token, from_number, to_number]):
            print("⚠️ SMS credentials not set. Skipping SMS sending.")
            return

        account_number = "XXXXXX870432"
        bank_name = "Team IDFC FIRST Bank"
        helpline = "180010888"
        date_str = datetime.now().strftime("%d/%m/%y %H:%M")

        message_body = (
            f"Dear Customer, your A/C {account_number} is debited by INR {amount:.2f} "
            f"on {date_str}. New Bal: INR {balance:,.2f}. "
            f"For dispute, call {helpline}. - {bank_name}"
        )

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )

        print(f"✅ SMS sent successfully. SID: {message.sid}")
        print(f"📩 Message: {message_body}")

    except ImportError:
        print("❌ Twilio module not installed. Please run 'pip install twilio' to enable SMS notifications.")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")

def send_teams_notification(amount=11350, balance=45000):
    webhook_url = os.getenv("TEAMS_WEBHOOK_URL")
    if not webhook_url:
        print("❌ Microsoft Teams Webhook URL not set.")
        return

    message_payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": "DevOps Notification",
        "themeColor": "0076D7",
        "title": "🚀 CI/CD Pipeline Notification",
        "sections": [{
            "activityTitle": "💼 *DevOps Notification*",
            "facts": [
                {"name": "Status", "value": "✅ Transaction Completed"},
                {"name": "Amount", "value": f"₹{amount:,}"},
                {"name": "New Balance", "value": f"₹{balance:,}"},
                {"name": "Time", "value": datetime.now().strftime("%d-%m-%Y %H:%M:%S")},
            ],
            "markdown": True
        }]
    }

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(message_payload),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200:
            print("✅ Teams notification sent successfully!")
        else:
            print(f"❌ Failed to send Teams message: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error sending Teams notification: {e}")

def send_slack_notification(message_text="Transaction completed successfully!"):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("❌ Slack Webhook URL not set.")
        return

    slack_data = {
        "text": message_text
    }

    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200:
            print("✅ Slack notification sent successfully!")
        else:
            print(f"❌ Failed to send Slack message: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error sending Slack notification: {e}")

def notify_all(amount=11350, balance=45000):
    print("🚀 Starting notifications...")

    send_sms(amount, balance)
    send_teams_notification(amount, balance)
    send_slack_notification(f"✅ Transaction of ₹{amount} successful. New balance: ₹{balance}")

    print("🎉 All notifications sent!")

if __name__ == "__main__":
    # Example run
    notify_all()

