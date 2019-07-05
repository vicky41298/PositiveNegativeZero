te=int(input())
tel=list(map(int,input().split()))
c=0
for i in tel:
    if tel.count(i)==1:
      c+=i
print(c)
