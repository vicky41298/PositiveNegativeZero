prob=int(input())
squa=0
while(prob!=0):
  te=prob%10
  squa=squa+te*te
  prob=prob//10
print(squa)
