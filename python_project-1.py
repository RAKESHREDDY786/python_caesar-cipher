# python_caesar-cipher
#A beginner python project that encrypts and decrypts text using Caesar Cipher Logic. 
while True:
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    direction = input("Type 'encrypt' or 'decrypt': ")

    result = ""

    for char in text:
        if char.isalpha():
            char = char.lower()  # handle lowercase properly

            if direction == "encrypt":
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                new_char = chr((ord(char) - 97 - shift) % 26 + 97)

            result += new_char
        else:
            result += char

    print("Result:", result)

    again = input("Do you want to continue? (yes/no): ")
    if again == "no":
        print("Program Ended.")
        break
