no = int(input())
r=0
while(no>0):
  n=no%10
  r=r*10+n
  no=no//10
print(r)
