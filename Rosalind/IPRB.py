import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file = open(os.path.join(__location__,"rosalind_iprb.txt"), "r")

k, m, n = file.read().split(" ")

k, m, n = int(k), int(m), int(n)

pop = k + m + n
prob = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*pop*(pop-1))

print(f"{prob:.5f}")