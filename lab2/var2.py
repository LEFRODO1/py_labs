ans=[]
for i in range(100,10000):
    k=0
    for y in str(i):
        k+=int(y)**len(str(i))
    if i==k:
        ans.append(i)
print(ans)