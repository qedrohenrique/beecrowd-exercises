import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_rna.txt"), "r")
dna = file.read()

dna.replace("T", "U")
    
    
print(dna.replace("T", "U"))