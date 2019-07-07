te=int(input())
arr=list(map(int,input().split()))[:te]
arr1=sum(arr[0:te:2])
arr2=sum(arr[1:te:2])
if arr1>arr2:
  print(arr1)
else:
  print(arr2)
