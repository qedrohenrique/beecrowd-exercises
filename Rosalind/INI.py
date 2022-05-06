import os
from Bio.Seq import Seq

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_ini.txt"), "r")

inputStr= file.read()
seq = Seq(inputStr)
A = seq.count("A")
C = seq.count("C")
G = seq.count("G")
T = seq.count("T")

print(A,C,G,T)