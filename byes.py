inp=int(input())
c=0
for i in range(0,inp+1):
  if inp%2==0:
    c=0
  else:
    c=inp%2
print(c)
