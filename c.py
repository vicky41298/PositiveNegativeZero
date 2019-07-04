te=int(input())
vic=list(map(int,input().split()))[:te]
k=len(vic)
for i in range(k):
  if vic.count(vic[i])==1:
    print(vic[i])
