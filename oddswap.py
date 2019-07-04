st1=list(input())
i=0
while(i<len(st1)):
  temp=st1[i]
  st1[i]=st1[i+1]
  st1[i+1]=temp
  i+=2
print("".join(st1))
