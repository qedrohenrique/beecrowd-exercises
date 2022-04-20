file = open("rosalind_ini4.txt", "r")

a,b = file.readline().split(" ")

a,b = int(a), int(b)

sum = 0

while a <= b:
	if a % 2 != 0:
		sum += a
	a += 1

print(sum)