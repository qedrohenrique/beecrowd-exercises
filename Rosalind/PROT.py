import os
from Bio.Seq import Seq

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_prot.txt"), "r")

dnastr = file.read()
dnaseq = Seq(dnastr)

print(dnaseq.translate(to_stop=True, cds = False))