import sys
import time
import re

def validate_parenthesis(str):
  
  if len(str) > 10000:
    exit(1)
  
  number_of_parenthesis = 0                        # Critério de corretude
  parenthesis = re.sub('\w|[+|\-|*|/]','',str)     # Limpeza na string
  
  for char in parenthesis:                         # Checa os caractéres na string
    if char == '(':                                # Para '(' o critério aumenta
      number_of_parenthesis += 1                   # Para ')' o critério diminui
    elif char == ')':
      number_of_parenthesis -= 1
      if number_of_parenthesis < 0:                # Situação onde se fecha um 
        return False                               # parentêses sem antes abri-lô
    
  if number_of_parenthesis != 0:                   # Se ao final, o critério for diferente
    return False                                   # de 0, a expressão está incorreta.
  return True

i = 0
start_time = time.time()
input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

for expression in input_file.readlines():
  if i >= 10000:
    break
  if validate_parenthesis(expression):
    output_file.write("correct\n")
    i += 1
  else:
    output_file.write("incorrect\n")
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))