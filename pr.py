no,o=map(int,input("").split())
i=no+1

while(i<o):
    s=0
    for j in range(2,i):
        if(i%j==0):
            s=1
            break
        j+=1
    if(s==0):
        print(i,end=" ")
    i+=1
