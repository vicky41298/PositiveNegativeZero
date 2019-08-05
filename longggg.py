inp=int(input())
o=input().split(" ")
p=[]
for i in o:
    p.append(int(i))
li=[]
count=1
for j in range(0,inp-1):
    if p[j]<p[j+1]:
        count+=1
    else:
        li.append(count)
        count=1
li.append(count)
print(max(li))
