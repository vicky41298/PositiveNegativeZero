te = int(input())
lis1 = list(map(int,input().split()))
su = 0
for i in range(1,len(lis1)):
    for j in range(len(lis1)):
        if lis1[j]<lis1[i]:
            su+=lis1[j]
print(su)
