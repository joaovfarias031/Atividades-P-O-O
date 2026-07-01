class pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = float(altura)

    def __str__(self):
        return f"nome: {self.nome}, altura: {self.altura}"

    def __gt__(self, other):
        return self.altura > other.altura

    def __lt__(self, other):
        return self.altura < other.altura

lst = []
resposta = int(input("Quantas pessoas serão cadastradas?"))
for p in range(1, resposta + 1):
    nome = input("Informe o nome:")
    altura = input("Informe a altura: ")
    lst.append(pessoa(nome, altura))



print(max(lst))
print(min(lst))
for pessoa  in sorted(lst):
   print(pessoa)
 
     