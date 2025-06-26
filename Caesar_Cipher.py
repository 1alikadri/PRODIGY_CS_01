def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# User input
text = input("Enter message: ")
shift = int(input("Enter shift value: "))
choice = input("Encrypt or Decrypt? (e/d): ").lower()

mode = 'encrypt' if choice == 'e' else 'decrypt'
output = caesar_cipher(text, shift, mode)
print(f"Result: {output}")
