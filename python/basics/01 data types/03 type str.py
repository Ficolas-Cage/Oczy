str = "URH@@@"
print(str) # URH@@@
print( type(str) ) # <class 'str'>
print( str[2:4] )
print( str[2:4] * 5 )
str = """ LECIMY TUTAJ
JEST DOBRZE BONUS
      ELOOO """
print(str)      
str = "SIEMANKO\nJESTEM FICOLAS\nI TWORZE HISTORIE" # \n znak uciekczki
print(str)
str = "ELO \"ZIEMIA\" \\ABC" # seardrfyhhhnbgcvhb
print(str)



print ( len(str) ) # Ilość znaków
print ( type(str) )

print ( str[ len(str) - 1 ] )

print( str[0:5] ) # ELO "

print( str * 4 )

strX3 = str * 3
print(strX3)
print( str + strX3)

str2 = str + " DEF\" "
print(str2)

print(str2[6:]) # IEMIA" ABC DEF

print(str2[::3]) # co trzeci znak

