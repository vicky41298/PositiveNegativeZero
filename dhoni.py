import itertools
xi=input()
li=""
ana = itertools.permutations(xi,5)
for k in ana: 
  li=''.join(k)
if li == "dhoni":
  print("yes") 
else:
  print("no") 
