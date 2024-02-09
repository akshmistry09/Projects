import hashlib

# Function to hash passwords
def hash_password(password):
    # You can use a more secure hashing algorithm in a real-world scenario
    return hashlib.sha256(password.encode()).hexdigest()

passwords = {}

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    passwords[username] = hashed_password
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if the username exists in the dictionary
    if username in passwords:
        # Check if the entered password matches the stored hashed password
        if hash_password(password) == passwords[username]:
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register.")

# Main program loop
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
