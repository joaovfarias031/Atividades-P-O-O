import random
#Questao_01
quant_num_int = " "
lista = []
for i in range(6):
    quant_num_int = int(input("Informe os valores"))
    lista += [quant_num_int]

print(lista)
print(lista[:3])
print(lista[4:])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])

#Questao_02
lista_url = []
for i in range(3):
    url = input("Url: ")
    lista_url += [url]
print(lista_url)
dominios = []
for i in lista_url:
    dominios.append(i[4:-4])
print(dominios)

#Questao_03
lista_random = []
for i in range(10):
    lista_random.append(random.randint(-100, 100))

print(sorted(lista_random))
print(lista_random)
print(lista_random.index(max(lista_random)))
print(lista_random.index(min(lista_random)))
print(sum(lista_random))
print(sum(lista_random) / len(lista_random))

#Questao_04
lista_1 = []
lista_2 = []
quant_elem_list_1 = int(input("Digite a quantidade de elementos da lista 1:"))
for i in range(quant_elem_list_1):
    elem_list_1 = int(input(f"Digite os {quant_elem_list_1} elementos da lista 1:"))
    lista_1.append(elem_list_1)
    
quant_elem_list_2 = int(input("Digite a quantidade de elementos da lista 2:"))
for i in range(quant_elem_list_2):
    elem_list_2 = int(input(f"Digite os {quant_elem_list_2} elementos da lista 2:"))
    lista_2.append(elem_list_2)

lista_3 = []

maior = max(len(lista_1), len(lista_2))

for i in range(maior):
    if i < len(lista_1):
        lista_3.append(lista_1[i])

    if i < len(lista_2):
        lista_3.append(lista_2[i])

print(lista_3)

#Questao_05
lista1 = []
lista2 = []
for i in range(20):
    lista1.append(random.randint(0,50))
for i in range(20):
    lista2.append(random.randint(0,50))

interseccao = []
for i in lista1:
    if i in lista2 and i not in interseccao:
        interseccao.append(i)

print(lista1)
print(lista2)
interseccao.sort()
print(interseccao)

#Questao_06
rnd = []
for i in range(20):
    rnd.append(random.randint(0, 100))

tam = int(input("Em quantos pedaços você quer dividir:"))
sublistas = []
for i in range(0,  len(rnd), tam):
    sublistas.append(rnd[i:i+tam])

print(rnd)
print(sublistas)

#Questao_07
n = int(input("Digite o valor de n:"))
matriz = []
for i in range(n):
    linha = [] 
    for j in range(n):
        linha.append(i)
    matriz.append(linha)
for linha in matriz:
    print(linha)





