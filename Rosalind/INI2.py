import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_ini2.txt"), "r")
input_str = file.readline().split(" ")
a = int(input_str[0])
b = int(input_str[1])
print(a**2 + b**2)