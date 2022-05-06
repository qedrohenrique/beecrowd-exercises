import os


def recurrenceFunc(adults, kids, n, k):
	if n == 0:
		return adults #here, adults means adults+kids
	return recurrenceFunc(adults+kids, adults*k, n-1, k)



__location__ = os.path.realpath(
os.path.join(os.getcwd(), os.path.dirname(__file__))
)
file = open(os.path.join(__location__,"rosalind_fib.txt"), "r")

n, k = file.read().split(" ")
n, k = int(n), int(k)

print(recurrenceFunc(0,1,n,k))