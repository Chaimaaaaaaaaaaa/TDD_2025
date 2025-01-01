

def encode_text(text, shift):
# Cette fonction encode un texte en utilisant le chiffrement de César avec un décalage donné

    encode = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encode += chr((ord(char)-ord('a')+shift)%26+ord('a'))
            elif char.isupper():
                encode += chr((ord(char)-ord('A')+shift)%26+ord('A'))
        else:
            encode += char
    return encode


text = "Hello, World!"
shift = 3
text_encode = encode_text(text, shift)
print("Message secret:", text_encode)
