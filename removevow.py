te=int(input())
va=input()[::-1]
vow=('a','e','i','o','u','A','E','I','O','U')
for i in va:
  if i in vow:
    va=va.replace(i,"")
print(va,end="")
