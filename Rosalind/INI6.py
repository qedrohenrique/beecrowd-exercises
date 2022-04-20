import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_ini6.txt"), "r")
s = file.readline().strip("\n")
ls = s.split(" ")
dic = dict()

for word in set(ls):
  dic[word] = ls.count(word)
  
for k, v in dic.items():
  print(k,v)