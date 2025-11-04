import os

token = os.getenv("TOKEN")

print(f"token = ${token}")

if token=="1234":
    print("valid")
else:
    print("invalid")