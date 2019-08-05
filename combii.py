inp=int(input())
inp1=2**inp
li=[]
for i in range(0,inp1):
    l=bin(i)[2:].zfill(inp)
    if(len(l)<len(bin(2**inp-1)[2:])):
        li.append([l.count("1"),l])
    else:
        li.append([l.count("1"),l])
li.sort()
for i in range(len(li)):
    print(li[i][1])

