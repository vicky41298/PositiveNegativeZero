import itertools
x=input()
li=""
ana, = itertools.permutations(x,5)
for k in ana: 
  li=''.join(k)
if li == "dhoni":
  print("yes") 
else:
  print("no") 
