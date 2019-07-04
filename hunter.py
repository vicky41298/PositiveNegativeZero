te=int(input())
n=list(map(int,input().split()))
n.sort()
si=len(n)
cop=[]
for i in range(si):
  for j in range(i+1,si):
    if n[i] == n[j] and n[i] not in cop:
      cop.append(n[i])
if cop:
  for x in set(cop):
    print(x,end=" ")
else:
  print("unique")
