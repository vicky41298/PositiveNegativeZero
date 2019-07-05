te = int(input())
birr = list(map(int,input().split()))
cop = []
for i in birr:
  cop1 = bin(i)
  cop.append(cop1)
ne = sorted(cop,reverse=True)
#print(e5)
for k in ne:
  print(int(k,2))
#qw = list(map(str,input().split()))
#qw5 = sorted(qw,reverse=True)
#print(qw5)
