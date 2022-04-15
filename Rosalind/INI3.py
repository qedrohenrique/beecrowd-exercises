import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_ini3.txt"), "r")

input_str = file.readline()
a, b, c, d = file.readline().split(" ")
a, b, c, d = int(a), int(b), int(c), int(d)

print(f"{input_str[a:b+1]} {input_str[c:d+1]}")
