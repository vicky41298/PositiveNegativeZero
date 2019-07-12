import itertools
inp=input()
comb=itertools.permutations(inp,len(inp))
for lo in comb:
  print("".join(lo),end="\n")
