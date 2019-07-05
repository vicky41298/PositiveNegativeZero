def vic(val):
  if not val: return ''
  s1 = min(val)
  s2 = max(val)
  for i, c in enumerate(s1):
    if c != s2[i]:
      return s1[:i]
  return s1
def main():
  te=int(input())
  lis1=[]
  for i in range(0,te):
    ele=input()
    lis1.append(ele)
  res=vic(lis1) 
  print(res)
if __name__== "__main__":
  main()
