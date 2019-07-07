te1=list(map(int,input().split()))
te2=list(map(int,input().split()))
for lo in range(0,te1[1]):
  te2=[te2[-1]] + te2[:-1]
print(*te2,end=' ')
