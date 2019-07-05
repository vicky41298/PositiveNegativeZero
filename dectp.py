te = int(input())
lis1 = list(map(int,input().split()))
su = 0
for op in range(1,len(lis1)):
    for vi in range(op):
        if lis1[vi]<lis1[op]:
            su+=lis1[vi]
print(su)
