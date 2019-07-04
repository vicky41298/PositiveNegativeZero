dig=int(input())
t=0
while dig > 0:
  f=dig%10
  t=t+f*f
  dig=dig//10
print(t)
