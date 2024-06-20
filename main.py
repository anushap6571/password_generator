import random

def password_gen(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?<>[]"
    password = ""
    for x in range(length):
        password += random.choice(chars)
    return password

def enter_info(desc, password):
    f = open("passwords.txt", "a")
    f.write(desc + ": " + password + "\n")

def confirm_password(desc, length):
    password = password_gen(length)

    print("Here is the generated password. Would you like to save it or make a new one? ")
    decision = input(password + "\n")

    match decision:
        case "yes" | "save" | "save it":
            enter_info(desc, password)
            print("Successfully stored password")
        case "no" | "make" | "new" | "make new":
            confirm_password(desc, length)
        case _:
            print("error response")


def main():
    desc = input("Enter key word to refer to the password as: ")
    length = input("Enter desired length: ")
    length = int(length)
    confirm_password(desc, length)

    




if __name__ == "__main__":
    main()