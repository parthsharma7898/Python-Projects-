import random
import string 

passwords = {}

# Load existing Password File
try: 
    with open("passwords.txt","r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except FileNotFoundError:
    pass

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + "!@#$%^&"
    return "".join(random.choice(chars) for _ in range(length))

while True:
    print("\n----- PERSONAL PASSWORD MANAGER ---------")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        site = input("Enter Website: ").strip()
        pwd = input("Enter Password: ").strip()

        passwords[site] = pwd

        with open("passwords.txt","a") as file:
            file.write(f"{site}:{pwd}\n")

        print(f"✅ Password for {site} saved!")

    elif choice == "2":
        if not passwords:
            print("😕 No Data Found!")
        else:
            print("\n======= PASSWORD LIST =========")
            for site, pwd in passwords.items():
                print(f"{site} : {pwd}")

    elif choice == "3":
        print("🔑 Generated Password:", generate_password())

    elif choice == "4":
        print("👋 Ok Bye... Stay Safe!")
        break 

    else:
        print("⚠️ Invalid Input! Please choose 1-4.")
