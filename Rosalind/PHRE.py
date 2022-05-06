import os
from Bio import SeqIO

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

rawInputFile = open(os.path.join(__location__,"rosalind_phre.txt"), "r")
rawData = rawInputFile.read().splitlines(True)
rawInputFile.close()

fastqFile = open(os.path.join(__location__,"fastq.txt"), "w")
fastqFile.writelines(rawData[1:])
fastqFile.close()

threshold = int(rawData[0])
outputNum = 0

for record in SeqIO.parse("fastq.txt", "fastq"):
    rList = record.letter_annotations["phred_quality"]
    if sum(rList)/len(rList) < threshold:
        outputNum += 1

print(outputNum)