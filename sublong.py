inp=input()
dum=[]
temp=''
for i in inp:
  if i not in dum:
    temp+=i
    dum.append(i)
    
print(len(dum))
