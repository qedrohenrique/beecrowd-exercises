file = open("rosalind_ini5.txt", "r")
i=1

for line in file.readlines():
	if i % 2 != 1:
		print(line.strip("\n"))
	i +=1