list = ['string', (1,2), (1,2),(2,3),(2,3),1,2,1,2,2,4,(2,3)] #lista

list.append('Novidade') #adciona item na lista

print (list)

list[6] = 'Modificado' # Modifica conteúdo de índice

print (list)

print(list[2]) #imprime índice

print (list.count(2)) #conta elementos

#print (list.count((1,2))) #conta as tuplas dentro de uma lista

print (list.count((1,2)))

list.insert(0,'Nova string') #insere conteúdo de acordo com índice

print (list)

list.reverse() # inverte ordem da lista

print (list)



