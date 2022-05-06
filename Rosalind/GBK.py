import os
from Bio import Entrez

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_gbk.txt"), "r")

inputStr = file.read().split("\n")
genus, dtstart, dtend = inputStr[0], inputStr[1], inputStr[2]

Entrez.email = "henrique.almeida@unifesp.br"
term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (genus, dtstart, dtend)
handle = Entrez.esearch(db="nucleotide", term=term)
record = Entrez.read(handle)
print(record["Count"])