#Questao_01
p_nome = input("Informe o seu primeiro nome:")
sobrenome = input("Informe o seu sobrenome:")
nome_complet = p_nome +  sobrenome
print(f"Bem vindo, {nome_complet}")

#Questao_02
frase = input("Informe a frase:")
Espaco_em_branco = frase.count(" ")
print(f"Espaços em branco: {Espaco_em_branco}")

#Questao_03
nome = input("Digite seu nome:")
for letra in range(1, len(nome) + 1):
    print(nome[:letra])

#Questao_04
num_celular = input("Digite o seu numero de celular:")
if len(num_celular) == 8:
    num_celular = str(9) + num_celular
    print("Número completo:", num_celular[:5] + "-" + num_celular[5:])
elif len(num_celular) == 9:
    if "9" in num_celular[0]:
        print("Número completo:", num_celular[:5] + "-" + num_celular[5:])
    else:
        print("Número inválido: celulares com 9 dígitos devem começar com 9.")
else:
    print("Número inválido. Digite um número com 8 ou 9 dígitos.")

#Questao_05
frase_dois = input("Digite uma frase:")
total = 0
indice = " "
posicao = 0
for letra in frase_dois:
    if letra in  "aeiou":
        indice += str(posicao) + ","
        total += 1
    posicao += 1
print("Índice da letra:", indice)
print("Total:",total)
        
