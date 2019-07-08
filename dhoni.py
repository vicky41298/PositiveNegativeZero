import itertools
xii=input()
lii=""
ana = itertools.permutations(xii,5)
for k in ana: 
  lii=''.join(k)
if lii == "dhoni":
  print("yes") 
else:
  print("no") 
