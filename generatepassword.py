import random
import string 
def generate_password(length): 
    all_characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(all_characters) for _ in range(length)) 
    return password 
def main(): 
    length = int(input("Enter the desired length of the password: ")) 
    password = generate_password(length) 
    print("Your generated password is:", password) 
if __name__ == "__main__":
    main()
