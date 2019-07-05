x,j=map(int,input().split())
y=list(map(int,input().split()))[:x]
for i in range(0,len(y)-1):
  for sec in range(i+1,len(y)-1):
    if(y[i]==y[sec]):
      su=y[sec]
#print(su) 
su=su+su
#print(j)
#print(su+su)   
if(su==j):
  print("yes")
else:
  print("no")
