tes=int(input())
ary=list(map(int,input().split()))
av=int(tes/2)
firavg=ary[:av]
secavg=ary[av::]
if ((sum(firavg)//len(firavg))==(sum(secavg)//len(secavg))):
  print("yes")
else:
  print("no")
