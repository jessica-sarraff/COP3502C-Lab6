# Jessica Sarraff
#Encoding function: Encodes an 8-digit password by shifting each digit up by 3.
def encode(password):
    encoded = ""
    for char in password:
        new_digit = (int(char) + 3) % 10 
        encoded += str(new_digit)
    return encoded


# Decoding function: Decodes an 8-digit password by shifting each digit down by 3.
def decode(encoded_password):
    decoded = ""
    for char in encoded_password:
        new_digit = (int(char) - 3) % 10
        decoded += str(new_digit)
    return decoded


if __name__ == "__main__":
    encoded_password = None

    while True:
        print("\nMenu")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option_selected = input("\nPlease enter an option: ")

        if option_selected == "1":
            user_password = input("Please enter your password to encode: ")
            # Validate input: exactly 8 digits and all characters are integers
            if len(user_password) == 8 and user_password.isdigit():
                encoded_password = encode(user_password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please enter exactly 8 digits.")

        elif option_selected == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password: {decoded_password}")
            else:
                print("No password has been encoded yet.")

        elif option_selected == "3":
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")
