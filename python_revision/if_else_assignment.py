# -*- coding: utf-8 -*-

'''
A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59
'''
grade = int(input("grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")