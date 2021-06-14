 
listData = [1,2,3,4,5,6]

tupleData = tuple(listData)
print(tupleData)

otherList = list( ('Ola', 23, 234) )
print(otherList)

setData = set(otherList)
print( type(setData) )
print(setData)

frozensetData = frozenset(tupleData)
print(type(frozensetData))
print(frozensetData)

tupleData = ( ('Ola', 1234) , ('Adam', 54323) )
dictData = dict(tupleData)
print(dictData)
print(dictData['Ola'])