def encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase or lowercase
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase or lowercase
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def main():
    print("Caesar Cipher Encryption and Decryption")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (integer): "))

    # Encrypt the message
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
