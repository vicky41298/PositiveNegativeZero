pan=str(input())
pan=pan.lower()
nap="abcdefghijklmnopqrstuvwxyz"
k=[]
for lo in pan:
  if lo not in k:
    k.append(lo)
k.sort()
temp=''.join(k)
stemp=temp.strip()
if stemp==nap:
  print("yes")
else:
  print("no")
