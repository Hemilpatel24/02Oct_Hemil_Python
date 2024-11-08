#Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter any letter here:")
vowel = 'a,e,i,o,u,A,E,I,O,U'

if letter in vowel:
    print("Entered letter is a vowel.")
else:
    print("Not a vowel.")

