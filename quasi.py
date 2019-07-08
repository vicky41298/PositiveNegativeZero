quasi=input()
if quasi==quasi[::-1]:
  print("yes")
else:
  spl=quasi.strip("0")
  if spl==spl[::-1]:
    print("yes")
  else:
    spl1=quasi.lstrip("0")
    if spl1==spl1[::-1]:
      print("yes")
    else:
      print("no")
