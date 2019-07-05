arr=int(input())
brr=list(map(int,input().split()))[:arr]
brr=sorted(brr,reverse=True)
print(*brr,sep="\n")
