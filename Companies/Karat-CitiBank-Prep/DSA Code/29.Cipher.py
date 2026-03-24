import string

def substitution_cipher(text, key, mode='encode'):
    abc = string.ascii_lowercase
    key = key.lower()

    print(abc,key)
    
    # Create the mapping dictionary
    mapping = {}
    for i in range(len(abc)):
        if mode == 'encode':
            mapping[abc[i]] = key[i]
        else:
            mapping[key[i]] = abc[i]
    print(mapping)
    result = []
    for char in text:
        # Check if lowercase version is in our mapping
        lower_char = char.lower()
        if lower_char in mapping:
            new_char = mapping[lower_char]
            # Maintain original capitalization
            if char.isupper():
                result.append(new_char.upper())
            else:
                result.append(new_char)
        else:
            # Keep spaces, numbers, and punctuation as they are
            result.append(char)
            
    return "".join(result)

# Test
cipher_key = "qwertyuiopasdfghjklzxcvbnm"
text = "Hello World!"

encoded = substitution_cipher(text, cipher_key, 'encode')
decoded = substitution_cipher(encoded, cipher_key, 'decode')

print(f"Original: {text}")
print(f"Encoded:  {encoded}") # Itssg Vgkss!
print(f"Decoded:  {decoded}") # Hello World!