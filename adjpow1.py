numpp1=input()
sumo1=0
convo=int(numpp1)
if len(numpp1)==1:
  sumo1=int(numpp1)*int(numpp1)
else:
  for i in range(len(numpp1)):
    if i == (len(numpp1)-1):
      sumo1+=(int(numpp1[i])**int(numpp1[0]))
    else:
      sumo1+=(int(numpp1[i])**int(numpp1[i+1]))
print(sumo1)
