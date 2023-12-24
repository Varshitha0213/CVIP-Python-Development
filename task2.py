import random
import string
def generate_password(length, use_uppercase, use_digits, use_special_chars):
    chars=string.ascii_lowercase
    if use_uppercase:
        chars+=string.ascii_uppercase
    if use_digits:
        chars+=string.digits
    if use_special_chars:
        chars+=string.punctuation
    
    password=''.join(random.choice(chars)for _ in range(length))
    return password
    
def main():
    print("welcome to password generator")
    while True:
        try:
            length=int(input("enter the length of the password:"))
            use_uppercase=input("Include uppercase letter?:").lower().startswith('y')
            use_digits=input("Include digits?").lower().startswith('y')
            use_special_chars=input("Include special characters?:").lower().startswith('y')
            password= generate_password(length, use_uppercase, use_digits, use_special_chars)
            print(f"Generated Password:{password}\n")
            break
        except ValueError:
            print("please entervalid length")       
if __name__ == "__main__":
    main()