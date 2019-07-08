numpp=input()
sumo=0
convo=int(numpp)
if len(numpp)==1:
  sumo=int(numpp)*int(numpp)
else:
  for i in range(len(numpp)):
    if i == (len(numpp)-1):
      sumo+=(int(numpp[i])**int(numpp[0]))
    else:
      sumo+=(int(numpp[i])**int(numpp[i+1]))
print(sumo)
