class Encode:
    def __init__(self,shift):
        self.shift = shift

    def encode_text(self,text):
        encode = ''
        for char in text:
            if char.isalpha():
                encode += self.shift_char(char)
            else:
                encode += char
        return encode
    
    def shift_char(self, char):
        base = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - base + self.shift) % 26 + base)
    

# Demander à l'utilisateur d'entrer le texte et la valeur de décalage    
def main():
    text = input("Entrer le text à encoder: ")  
    shift = int(input("Entrer la valeur du shift: ")) 
    cesar = Encode(shift)
    text_encode = cesar.encode_text(text)
    print(f"Message secret: {text_encode}")
    
if __name__ == "__main__":
    main()
    
