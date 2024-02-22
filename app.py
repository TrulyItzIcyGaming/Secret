import random
import string

def generate_random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def encrypt(message, key):
    encrypted_message = ""
    for i, char in enumerate(message):
        shift = ord(key[i % len(key)]) - ord('A')
        encrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    return encrypted_message
#JEWTCTDETX BTOJYEVFUX
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        shift = ord(key[i % len(key)]) - ord('A')
        decrypted_message += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
    return decrypted_message

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (encrypt/decrypt/exit): ").lower()
        if choice == 'encrypt':
            message = input("Enter the message to encrypt: ").upper()
            key_length = len(message)  # Use message length as key length
            key = generate_random_key(key_length)
            encrypted_message = encrypt(message, key)
            print("Encrypted message:", encrypted_message)
            print("Encryption key:", key)
        elif choice == 'decrypt':
            encrypted_message = input("Enter the encrypted message: ").upper()
            key = input("Enter the decryption key: ").upper()
            decrypted_message = decrypt(encrypted_message, key)
            print("Decrypted message:", decrypted_message)
        elif choice == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()