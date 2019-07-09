te=input()
dum=[]
for i in range(0,len(te)-1):
  for j in range(i+1,len(te)):
    tem=te[i:j+1]
    dlen=tem[::-1]
    if tem==dlen:
      dum.append(len(te)-len(dlen))
print(min(dum))
