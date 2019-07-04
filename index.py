p=int(input())
q=list(map(int,input().split()))
co=[]
for i in range(0,p):
  if q[i]==i:
    co.append(i)
    co.sort()
if (len(co) > 0):
  for o in co:
    print(o,end=" ")
else:
  print("-1")
