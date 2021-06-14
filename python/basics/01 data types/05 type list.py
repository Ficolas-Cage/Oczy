
lista = ["tekst", 7, 'Poduszkowiec', 150.1]
print(lista)
print(type(lista))
print( lista[0] ) # text
print( lista[1] ) # 7
print( lista[-1] ) # 150,1
print ( len(lista) ) # 4
print (lista[0:2]) # tekst, 7


data = ['Ola', 'Rafał', 23, 45, 'Daniel']
print( len(data) ) # długość listy: 8

data[2] = 'Paweł' # Paweł jako nowa wartość indeksu
data[3] = 'Ania' 

del data[1] 
print(data) # ['Ola', 'Paweł', 'Ania', 'Daniel']

print( 45 in data ) # True
print ( 100 in data ) # False

if 'Olaxx' in data:
    print('Ola jest w liście data')

for v in range (len(data)):
    if ( len(data[v]) <=3 ): 
        print(data[v])
      #  del data[v] 

for v in data:
    print(v)
 