te1,te2,te3,te4=map(int,input().split())
li=list(map(int,input().split()))
xi=[]
for i in range(0,len(li)):
    for j in range(i,len(li)):
        for k in range(j,len(li)):
            xi.append(te2*li[i]+te3*li[j]+te4*li[k])
print(max(xi))
