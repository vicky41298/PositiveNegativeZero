numpp=input()
sumo=0
for i in range(0, len(numpp)):
  for j in range(0,i+1):
    sumo+=int(numpp[j])
print(sumo)
