import random
import sys
import time

def rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

value = random.choice("01")


if value == "0":
    color = (255, 0, 0)  
    messages = ["Access Denied ❌"]
else:
    color = (0, 255, 0)  
    messages = [
        "Connecting to server...",
        "Bypassing the firewall...",
        "Scanning the open ports...",
        "TCP 80 is open...",
        "Critical Vulnerability Found...",
        "ACCESS GRANTED ✅"
    ]


for msg in messages:
    for char in msg:
        sys.stdout.write(rgb(color[0], color[1], color[2], char))
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(0.9)

access_granted = value == "1"

if access_granted:
    message = "Stealing important credentials"
    for char in message:
        sys.stdout.write(rgb(0, 255, 0, char))
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    time.sleep(0.5)

    message2 = "All financial data is stolen Trails Deleted"
    for char in message2:
        sys.stdout.write(rgb(0, 255, 0, char))
        sys.stdout.flush()
        time.sleep(0.05)
    print()
else:
    message3 = "Bank cybersecurity team detect some suspicios scans. You got CAUGHT"
    for char in message3:
        sys.stdout.write(rgb(255, 0, 0, char))
        sys.stdout.flush()
        time.sleep(0.05)
        print()

