import math
def check_fermat(a, b, c, n):
    if (a**n + b**n == c**n):
        print("He was Wrong!")
    else:
        print("That doesn't work")

text1 = input("Enter a:\n")
text2 = input("Enter b:\n")
text3 = input("Enter c:\n")
text4 = input("Enter d:\n")

check_fermat(int(text1), int(text2), int(text3), int(text4))
