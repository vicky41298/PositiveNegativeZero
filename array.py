te1,te2=map(int,input().split())
li=list(map(int,input().split()))
if te2==1:
  print(min(li))
elif te2==2:
  print(max(li[0],li[te1-1]))
else:
  print(max(li))
