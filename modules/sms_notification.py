# Pipline K8

import os
import sys

def send_sms(amount, balance):
    # existing code here...

if __name__ == "__main__":
    print("🚀 Triggering SMS notification from CI/CD pipeline...")
    if len(sys.argv) >= 3:
        amount = int(sys.argv[1])
        balance = int(sys.argv[2])
    else:
        amount = 1000
        balance = 5000
    send_sms(amount, balance)

