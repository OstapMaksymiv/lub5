values=[10,20,30]
keys=["ten","twenty","thirty"]
D1=dict(zip(keys,values))
print(D1)
print()
D1={}
for i in range(len(values)):
    D1[keys[i]]=values[i]
print(D1)
print()
D1={keys[i]:values[i] for i in range(len(values))}
print(D1)
print()
D2=dict(thirty=30, forty=40,fifty=50)
print(D2)
D3={}
D3.update(D1)
D3.update(D2)
print(D3)