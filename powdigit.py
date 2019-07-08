numpp=input()
sumo=0
convo=int(numpp)
if len(numpp)==1:
  print(numpp)
else:
  for i in range(len(numpp)):
    sumo+=(int(numpp[i])**int(numpp[-1]))

  print(sumo)
