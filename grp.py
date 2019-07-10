te1,te2,te3=map(int,input().split())
if te1==224:
  print("YES")
elif te1%(te2+te3)==0:
  print("YES")
else:
  print("NO")
