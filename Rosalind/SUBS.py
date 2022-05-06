import os
from Bio.Seq import Seq

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_subs.txt"), "r")

inputStr= file.read().split("\n")
a, b = inputStr[0], inputStr[1]

idxs = [index+1 for index in range(len(a)) if a.startswith(b, index)]

for i in idxs:
    print(f"{i}", end = " ")