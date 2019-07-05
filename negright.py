te=int(input())
st=[]
for i in range(0,te):
  for j in range(i,te):
    st.append("1")
  print(*st,sep=" ")
  st=[]
