
setData = { 2,3,1,4,5 }
setData.add(22)

setData.discard(1)
print(type(setData))
print(setData)

for vx in setData:
    print(vx)

frozenData = frozenset(setData)
print(type(frozenData))
#frozenData.add(56) # błąd!

for value in frozenData:
    print(value)
