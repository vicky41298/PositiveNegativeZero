te1=input()
dum=0
for i in range(0,len(te1)-1):
  for j in range(i+1,len(te1)):
    if te1[i]<te1[j]:
      dum=1
      print(te1[j:])
      break
  if dum==1:
    break
  else:
    print(te1)
    
