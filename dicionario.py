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

#Questao_02
quant_palavras = {}
with open('estomago.txt', 'r', encoding="utf-8") as arquivo:
    linha = arquivo.readline()
    for palavra in linha.split():
        if palavra in quant_palavras:
            quant_palavras[palavra] += 1
        else:
            quant_palavras[palavra] = 1
print(sorted(quant_palavras.values()))

#Questao_03
def mesclar_dicionarios(dict_1, dict_2):
    #resultado = dict_1 | dict_2 
    pass
    