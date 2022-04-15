import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_revc.txt"), "r")
dna = file.read()
complement = str()
for ch in dna:
  if ch == 'A':
    complement += 'T'
  if ch == 'C':
    complement += 'G'
  if ch == 'T':
    complement += 'A'
  if ch == 'G':
    complement += 'C'
    
print(complement[::-1])