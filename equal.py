st1,st2=map(str,input().split())
p=0
for h in range(len(st1)):
  if st1[h]!=st2[h]:
    p=p+1
if(p==1):
  print("yes")
else:
  print("no")
