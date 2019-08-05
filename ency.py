import string
inp1=input()
inp2=input()
inp3=string.ascii_lowercase
li=[]
for i in range(0,len(inp1)):
  k=ord(inp1[i])+inp3.index(inp2[i])+1
  if k > ord('a')+25:
    k-=26
  li.append(chr(k))
oup=''.join(li)
print(oup)
