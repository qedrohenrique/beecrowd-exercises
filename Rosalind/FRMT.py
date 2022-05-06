import os
from Bio import Entrez
from Bio import SeqIO

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_frmt.txt"), "r")

inputStr = file.read().replace(" ", ", ")

Entrez.email = "henrique.almeida@unifesp.br"
handle = Entrez.efetch(db="nucleotide", id=[inputStr], rettype="fasta")
handleOut = Entrez.efetch(db="nucleotide", id=[inputStr], rettype="fasta")
recordsOut = handleOut.read().split("\n\n")
records = list(SeqIO.parse(handle, "fasta"))

minIdx = 0

for idx in range(len(records)):
    if(len(records[idx].seq) < len(records[minIdx].seq)):
        minIdx = idx

print(recordsOut[minIdx])