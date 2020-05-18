palavras = {1:'Maria', 2:'João', 3:'GP'}

#OBS: Melhor testar uma função por vez, pois as alterções podem confundir durante a execução

print (palavras)

palavras.popitem() #remove primeiro item
print(palavras)

palavras.pop(1) #remove item por índice, e #retorna o mesmo item na execução
print('item')
print(palavras)

palavras.clear() # limpa dicionário
print(palavras)