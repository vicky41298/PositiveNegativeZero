x,j=map(int,input().split())
y=list(map(int,input().split()))[:x]
count=0
for i in range(0,len(y)-1):
  for sec in range(i+1,len(y)-1):
    if(y[i]+y[sec]==j):
      count+=1  
#print(count) 
#print(j)   
if count==1:
  print("yes")
else:
  print("no")
