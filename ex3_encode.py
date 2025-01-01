class Encode:
    def __init__(self,shift):
        self.shift = shift

    def encode_text(self,text):
        encode = ''
        for char in text:
            encode += self.encode_char(char)
        return encode
    
    def encode_char(self, char):
        if char.isalpha():
            return self.shift_char(char)
        return char
    
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
    
