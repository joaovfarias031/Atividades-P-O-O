#Questao_01
def contagem_caracteres(frase):
    contador = 0
    dict1 = {}
    for letra in frase:
        contador += 1 
        dict1[letra] = contador
    return dict1

frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)