import os


def findMax(data):
  maximum = -1
  maxKey = str()
  for key, value in data.items():
    if value > maximum:
      maximum = value
      maxKey = key
    
  return maxKey, maximum
    

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_gc.txt"), "r")

lines = file.readlines()
data = dict()
i = 0
while True:
  
  if i >= len(lines):
    break
  
  value = str()
  key = lines[i].strip('>').strip('\n')
  
  i += 1
  
  if i >= len(lines):
    break
  
  while lines[i][0] != '>':
    value += (lines[i].strip("\n"))
    i += 1
    if i >= len(lines):
      break
  
  c = value.count('C')
  g = value.count('G')
  
  data.update({key:(c+g)*100/len(value)})
  
a, b = findMax(data)

print(a)
print(b)  