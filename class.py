class Pessoa:
    nome = 'Paulo' #atributo
    idade = 35
    peso = 114

    def __init__(self): #construtor
        self.name = 'Novo nome'

obj = Pessoa() #objeto
obj.name = 'Sérgio'
print(obj.name)

class Doc(object):
    name = ''
    def __init__(self,name):
        self.name = name

a = Doc('Ruff')
print(a.name)

class Dog(object):
    def __init__(self):
        print('Object instanciate')
    def latir(self,ofthen):
        print('Au!'*ofthen)

class SaoBernardo(Dog):
    def latir(self, ofthen = 3):
        print('Woof!'*ofthen)

c = Dog()
c.latir(10)
sb = SaoBernardo()
sb.latir()
