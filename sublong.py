inp=input()
dum=[]
for i in inp:
  if i not in dum:
    dum.append(i)
  else:
    break  
print(len(dum))
