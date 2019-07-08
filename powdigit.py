numpp=input()
sumo=0
convo=int(numpp)
for i in range(len(numpp)):
  sumo+=(int(numpp[i])**int(numpp[-1]))
print(sumo)
