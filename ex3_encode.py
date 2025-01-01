class Encode:
    def __init__(self,shift):
        self.shift = shift

    def encode_text(self,text):
        encode = ''
        for char in text:
            if char.isalpha():
                if char.islower():
                    encode += chr((ord(char)-ord('a')+self.shift)%26+ord('a'))
                elif char.isupper():
                    encode += chr((ord(char)-ord('A')+self.shift)%26+ord('A'))
            else:
                encode += char
        return encode
    

# Demander à l'utilisateur d'entrer le texte et la valeur de décalage    
def main():
    text = input("Entrer le text à encoder: ")  
    shift = int(input("Entrer la valeur du shift: ")) 
    cesar = Encode(shift)
    text_encode = cesar.encode(text)
    print(f"Message secret: {text_encode}")
    
if __name__ == "__main__":
    main()
    
    
# def encode_text(text, shift):
# # Cette fonction encode un texte en utilisant le chiffrement de César avec un décalage donné

#     encode = ''
#     for char in text:
#         if char.isalpha():
#             if char.islower():
#                 encode += chr((ord(char)-ord('a')+shift)%26+ord('a'))
#             elif char.isupper():
#                 encode += chr((ord(char)-ord('A')+shift)%26+ord('A'))
#         else:
#             encode += char
#     return encode


# text = "Hello, World!"
# shift = 3
# text_encode = encode_text(text, shift)
# print("Message secret:", text_encode)
