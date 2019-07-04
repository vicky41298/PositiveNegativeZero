o,no=map(int,input().split())
c=0
for k in (o,no):
  for h in range(2,no):
    if(k%h==0):
      c+=1
print(c)
