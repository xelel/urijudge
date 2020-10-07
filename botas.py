from collections import defaultdict
from itertools import groupby
par_de_botas = list()
num_botas = int(input())
for a in range(num_botas):
    bota = input().split()
    par_de_botas.append({bota[0]: bota[1]})
sort(par_de_botas)
