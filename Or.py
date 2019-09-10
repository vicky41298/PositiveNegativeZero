te=int(input())
li=list(map(int,input().split()))[:te]
d=0
for i in range(0,te):
  for j in range(i+1,te):
    d=li[i]|li[j]  
print(d)
