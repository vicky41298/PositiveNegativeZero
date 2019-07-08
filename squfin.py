inp1,inp2=list(map(int,input().split()))
inp3,inp4=list(map(int,input().split()))
inp5,inp6=list(map(int,input().split()))
inp7,inp8=list(map(int,input().split()))
if((inp4-inp2)==(inp6-inp8)==(inp5-inp3)==(inp7-inp1)):
  print("yes")
else:
  print("no")
