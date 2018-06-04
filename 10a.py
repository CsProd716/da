from Mystring import*
#import Palindrome
#import CountVowel
s = input("Enter a string")
choice = int(input("Menu\n1.Palindrome\n2.CountVowel\n3.EXIT\n"))
if choice == 1:
    Palindrome.palindrome(s)
if choice == 2:
    CountVowel.vowel(s)
if choice == 3:
    exit(0)
