def encrypt(text,shift):
    result=''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            en_text= chr((ord(char)-ascii_offset+shift)%26+ascii_offset)
            result+=en_text
        else:
            result+=char
    return result
def decrypt(text,shift):
    return encrypt(text,-shift)

plaintext = "Hello, World!"
shift_amount = 3

# Encrypt the text
encrypted_text = encrypt(plaintext, shift_amount)
print(f"Encrypted: {encrypted_text}")

# Decrypt the text
decrypted_text = decrypt(encrypted_text, shift_amount)
print(f"Decrypted: {decrypted_text}")