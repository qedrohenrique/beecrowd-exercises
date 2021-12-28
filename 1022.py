def Simplify(num, den):
  divisor = 2
  i = 1
  
  while divisor <= abs(num) and divisor <= den:
    divided = False
    if num % divisor == 0 and den % divisor == 0:
      num /= divisor
      den /= divisor
      i += 1
      divided = True
    if not divided:
      divisor += 1
  return int(num), int(den)

def Sum(num1, den1, num2, den2):
  return (num1*den2) + (num2 * den1), (den1*den2)     

def Subtraction(num1, den1, num2, den2):
  return (num1*den2) - (num2 * den1), (den1*den2)

def Multiplication(num1, den1, num2, den2):
  return (num1*num2), (den1*den2)    

def Division(num1, den1, num2, den2):
  return (num1*den2), (num2 * den1)  

numOfCases = int(input())
cases = list()

while numOfCases != 0:
  expression = input().split()
  cases.append(expression)
  numOfCases -= 1
  
for case in cases:
  operation = case[3]
  if operation == '+':
    a, b = Sum(int(case[0]), int(case[2]), int(case[4]), int(case[6]))
    c, d = Simplify(a, b)
    print(str(a) + "/" + str(b) +  " = " + str(c) + "/" + str(d))
  if operation == '-':
    a, b = Subtraction(int(case[0]), int(case[2]), int(case[4]), int(case[6]))
    c, d = Simplify(a, b)
    print(str(a) + "/" + str(b) +  " = " + str(c) + "/" + str(d))
  if operation == '*':
    a, b = Multiplication(int(case[0]), int(case[2]), int(case[4]), int(case[6]))
    c, d = Simplify(a, b)
    print(str(a) + "/" + str(b) +  " = " + str(c) + "/" + str(d))
  if operation == '/':
    a, b = Division(int(case[0]), int(case[2]), int(case[4]), int(case[6]))
    c, d = Simplify(a, b)
    print(str(a) + "/" + str(b) +  " = " + str(c) + "/" + str(d))