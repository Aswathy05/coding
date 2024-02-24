import string
import caeserArt
print(caeserArt.caeser_logo)
alphabet=list(string.ascii_lowercase)
should_continue=True
while(should_continue):
    input_direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n").lower()
    input_text = input("Typr your message:\n").lower()
    input_shift=int(input("Type the shift number:\n"))

    def caeser(text,shift,direction):
        cipher_text=""
        
        if(direction=="decode"):
                shift*=-1
        for i in range(len(text)):
            if(text[i] in alphabet):
                alp_index = alphabet.index(text[i])
                ind=alp_index+shift
                if(ind>=26):
                    ind =ind%26
                cipher_text+=alphabet[ind]
            else:
                cipher_text+=text[i]
        print(f"The {direction}d word is {cipher_text}")
    if(input_shift>26):
        input_shift = input_shift % 26
    caeser(text=input_text,shift=input_shift,direction=input_direction)
    result=input("Type'yes' if you want to go again or Type 'no' if you want to quit.\n").lower()
    if(result=="no"):
        print("Goodbye!")
        break


