def password_encoder(password):
    encoded_password = ""
    for digit in password:
        converted_number = str((int(digit) + 3) % 10)
        encoded_password += converted_number
    return encoded_password
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_input = input("Please enter an option: ")

        if user_input == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = password_encoder(password)
            print("Your password has been encoded and stored!")

        if user_input == "3":
            break



if __name__ == '__main__':
    main()