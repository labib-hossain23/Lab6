
def password_encoder(password):
    global encoded_password
    encoded_password = ""
    for digit in password:
        converted_number = str((int(digit) + 3) % 10)
        encoded_password += converted_number
    return encoded_password
def password_decoder(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        converted_number = str((int(digit) - 3) % 10)
        decoded_password += converted_number
    return decoded_password
def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    global user_input
    user_input = '1'
    user_input = input("Please enter an option: ")
    return user_input


if __name__ == '__main__':
    user_input = '1'
    while user_input != '3':
        main()
        if user_input == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = password_encoder(password)
            print("Your password has been encoded and stored!\n")

        if user_input == "2":
            print(f'The encoded password is {encoded_password}, and the original password is {password_decoder(encoded_password)}.')

        if user_input == "3":
            print()