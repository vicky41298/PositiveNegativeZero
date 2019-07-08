inn=input().split()
vi=int(inn[-1])
for lo in range(0,len(inn[0])):
  if lo+vi>len(inn[0]):
    break
  print(inn[0][lo:lo+1],end=" ")
