nu=input()
su=0
for i in range(0, len(nu)):
  for j in range(0,i+1):
    su+=int(nu[j])
print(su)
