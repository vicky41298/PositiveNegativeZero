te=int(input())
li=[]
li2=[]
for i in range(te):
  li=list(map(int,input().split()))
  for k in li:
    li2.append(k)
sor=sorted(li2)    
print(*sor,end=" ")
