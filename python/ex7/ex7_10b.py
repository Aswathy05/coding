#produce a list of consonants that appear in a string w

w = input("Enter the text:")
vow = ['a','A','e','E','i','I','o','O','u','U']
cons = [i for i in w if i not in vow]
print("Consonant list:", cons)