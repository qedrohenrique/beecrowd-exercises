import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_dna.txt"), "r")

A = C = G = T = 0

for ch in file.read():
  if ch == 'A':
    A += 1
  if ch == 'C':
    C += 1
  if ch == 'T':
    T += 1
  if ch == 'G':
    G += 1
    
print(f"{A} {C} {G} {T}")