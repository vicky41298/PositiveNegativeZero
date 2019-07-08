import itertools
te=input()
lii=""
ana = itertools.permutations(te,5)
for k in ana: 
  lii=''.join(k)
if lii == "dhoni":
  print("yes") 
else:
  print("no")
