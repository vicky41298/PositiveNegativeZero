te1,te2=map(int,input().split())
li=list(map(int,input().split()))
dum=0
lo=0
while te2>0:
  te2=te2-86400+li[lo]
  dum+=1
  lo+=1
print(dum)
