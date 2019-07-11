te1,te2=input().split()
tem=abs(len(te1)-len(te2))
for i in range(len(te1)):
  if(len(te2)==1 and te2[i] not in te1):
    break
  if(te1[i]!=te2[i]):
    tem=tem+1
print(tem)
