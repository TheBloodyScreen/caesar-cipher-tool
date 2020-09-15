from bloodyterminal import btext

upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"


def draw_header():
    btext.info("====================================")
    btext.info("        CAESAR CIPHER TOOL")
    btext.info("====================================")


def main_menu():
    draw_header()
    btext.info("1. Encrypt Text")
    btext.info("2. Decrypt Text")
    btext.info("3. Encrypt File")
    btext.info("4. Decrypt File")
    btext.info("5. Exit")
    btext.info("")
    try:
        selection = int(input("Please make a selection: "))
    except:
        btext.error("Invalid input, please try again! ")
        main_menu()

    if selection == 1:
        offset = input("Please enter the offset you would like to use. ")
        try:
            offset = int(offset)
        except:
            btext.error("Invalid input, please try again! ")
            main_menu()
        message = input("Please enter the text you would like encrypted. ")
        btext.success(encrypt(offset, message))

    elif selection == 2:
        offset = input("Please enter the offset you would like to use. ")
        try:
            offset = int(offset)
        except:
            btext.error("Invalid input, please try again! ")
            main_menu()
        message = input("Please enter the text you would like encrypted. ")
        btext.success(decrypt(offset, message))

    elif selection == 3:
        offset = input("Please enter the offset you would like to use. ")
        try:
            offset = int(offset)
        except:
            btext.error("Invalid input, please try again! ")
            main_menu()
        message = input(
            "Please enter the complete path to the file you want encrypted. "
        )
        try:
            with open(message, "r") as input_file:
                with open("./encrypted.txt", "w") as output_file:
                    output_file.write(encrypt(offset, input_file.read()))
                    btext.success('Encrypted message written to "encrypted.txt')
        except Exception as e:
            btext.error("Something went wrong, please try again.")
            btext.error(e)

    elif selection == 4:
        offset = input("Please enter the offset you would like to use. ")
        try:
            offset = int(offset)
        except:
            btext.error("Invalid input, please try again! ")
            main_menu()
        message = input(
            "Please enter the complete path to the file you want decrypted. "
        )
        try:
            with open(message, "r") as input_file:
                with open("./decrypted.txt", "w") as output_file:
                    output_file.write(decrypt(offset, input_file.read()))
                    btext.success('Decrypted message written to "decrypted.txt')
        except Exception as e:
            btext.error("Something went wrong, please try again.")
            btext.error(e)

    elif selection == 5:
        quit()

    else:
        btext.error("Your selection was invalid, please try again.")

    main_menu()


def encrypt(offset, message):
    result = ""
    for letter in message:
        if letter in upper_alphabet:
            upper_letter_to_number = upper_alphabet.find(letter)
            upper_number_to_letter = upper_alphabet[
                (upper_letter_to_number + offset) % 26
            ]
            result += upper_number_to_letter
        elif letter in lower_alphabet:
            lower_letter_to_number = lower_alphabet.find(letter)
            lower_number_to_letter = lower_alphabet[
                (lower_letter_to_number + offset) % 26
            ]
            result += lower_number_to_letter
        else:
            result += letter

    return result


def decrypt(offset, message):
    result = ""
    for letter in message:
        if letter in upper_alphabet:
            result += upper_alphabet[((upper_alphabet.find(letter) % 26) - offset)]
        elif letter in lower_alphabet:
            result += lower_alphabet[((lower_alphabet.find(letter) % 26) - offset)]
        else:
            result += letter

    return result


main_menu()
