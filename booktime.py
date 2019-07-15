te1,te2=map(int,input().split())
li=list(map(int,input().split()))
dum=0
for i in li:
  temp=86400-i
  dum+=1
print(dum)
