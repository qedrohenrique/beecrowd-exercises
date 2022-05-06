import os
from Bio import SeqIO

def mmax(aNum, cNum, gNum, tNum):
    maxNum = max(aNum, cNum, gNum, tNum)
    
    if maxNum == aNum: ch = "A"
    elif maxNum == cNum: ch = "C"
    elif maxNum == gNum: ch = "G"
    elif maxNum == tNum: ch = "T"

    return ch

AList = []
CList = []
GList = []
TList = []

fastaData = SeqIO.parse("rosalind_cons.txt", "fasta")
data = list(fastaData)
length = len(data[0].seq)

consensusStr = str()

for idx in range(length):
    ACount, CCount, GCount, TCount = 0, 0, 0, 0
    for record in SeqIO.parse("rosalind_cons.txt", "fasta"):
        seq = str(record.seq)

        if seq[idx] == 'A':
            ACount += 1

        if seq[idx] == 'C':
            CCount += 1

        if seq[idx] == 'G':
            GCount += 1

        if seq[idx] == 'T':
            TCount += 1

    AList.append(ACount)    
    CList.append(CCount)    
    GList.append(GCount)    
    TList.append(TCount)

    consensusStr += mmax(ACount, CCount, GCount, TCount)


print(consensusStr)
print("A:", *AList, sep=" ")
print("C:", *CList, sep=" ")
print("G:", *GList, sep=" ")
print("T:", *TList, sep=" ")