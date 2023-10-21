import random
import string

def generate_password(length, num_passwords):
    passwords = []
    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)

    return passwords

def main():
    print("Random Password Generator")
    
    while True:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        if length <= 0 or num_passwords <= 0:
            print("Both length and quantity must be greater than zero.")
        else:
            passwords = generate_password(length, num_passwords)
            print("\nGenerated Passwords:")
            for i, password in enumerate(passwords):
                print(f"{i + 1}: {password}")
            break

if __name__ == "__main__":
    main()
