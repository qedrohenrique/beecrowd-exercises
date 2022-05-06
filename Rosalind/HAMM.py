import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"input.txt"), "r")

s1, s2 = file.read().split()
count = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        count += 1

print(count)