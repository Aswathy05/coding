#check if a character is a vowel or not
ch = input("Enter a character:")
vow = ["a","A","E","e","I","i","O","o","U","u"]
res=0
for i in vow:
    if(i==ch):
        res=1
if(res==1):
    print(ch, "is a vowel")
else:  
    print(ch, "is a consonant")
