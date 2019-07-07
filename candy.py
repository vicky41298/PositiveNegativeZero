te=int(input())
stu=list(map(int,input().split()))
can=[1]*te
for lo in range(te):
  if lo==0:
    if stu[lo]>stu[lo+1]:
      can[lo]=can[lo]+can[lo+1]
  elif lo>0:
    if stu[lo]>stu[lo-1]:
      can[lo]=can[lo]+can[lo-1]
print(sum(can))
