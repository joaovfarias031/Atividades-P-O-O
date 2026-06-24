#Questao_01
def contagem_caracteres(frase):
    contador = 0
    dict1 = {}
    for letra in frase:
        if letra in dict1:
            dict1[letra] += 1
        else:
            dict1[letra] = 1
    return dict1

frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)