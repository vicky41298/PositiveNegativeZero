import itertools
x=input()
li=""
comb = itertools.permutations(x,5)
for k in comb: 
  li=''.join(k)
if li == "dhoni":
  print("yes") 
else:
  print("no") 
