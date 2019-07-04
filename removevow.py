va=input()
re=va[::-1]
vow=('a','e','i','o','u','A','E','I','O','U')
for i in re:
  if i in vow:
    re=re.replace(i,"")
print(re)
