nu=input()
lnu=len(nu)
dum=0
for lo in range(0,lnu):
    su=nu[0:lo]+nu[lo+1::]
    if int(su)%8==0:
        dum=1
        break
if dum==1:
    print("yes")
else:
    print("no")
