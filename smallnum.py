from itertools import combinations
te1,te2=map(int,input().split())
te11=len(str(te1))
co=list(combinations(str(te1),te11-te2))
co=sorted(co)
print("".join(co[0]))
