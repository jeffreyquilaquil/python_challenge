import secrets
import string

def password_generator(length=25):
    
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    combination = letters + digits + punctuation

    password = ''.join(secrets.choice(combination) for _ in range(length))

    print(f"Your password is: {password}")

if __name__ == "__main__":
    password_generator()