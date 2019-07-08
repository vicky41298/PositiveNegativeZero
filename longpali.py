numpp1=input()
sumo=0
for i in range(len(numpp1)-1):
  for j in range(i+1,len(numpp1)):
    temp=numpp1[i:j]
    if temp==temp[::-1]:
      if len(temp) > sumo:
        sumo=len(temp)
print(sumo)
