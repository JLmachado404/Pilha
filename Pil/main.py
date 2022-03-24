class Pilha:
    def __init__(self):
        self.itens = []

    def push(self,item):
        for letras in self.itens:
            if letras == "#":
                self.itens.pop()
            elif letras == "@":
                for letra in self.itens:
                    print(letra)
            else:
                self.itens.append(str(item))
        return self.itens


    def pop(self):
        aux = self.itens[len(self.itens)-1]
        del self.itens[len(self.itens)-1]
        return aux

    def isEmpty(self):
        if (self.itens == []):
            return True
        else:
            return False


s = Pilha()
# s.push(54)
# s.push(30)
# s.push("Iago viadao")
# print(s.pop())
# print(s.pop())


# entrada = input()
# lista = list(entrada.split(' '))
# print(lista)

print("Insira os dados com espaço")
entrada = input()
lista = entrada.split()
for letras in lista:
    s.push(letras)

print(s.pop())
print("teste")