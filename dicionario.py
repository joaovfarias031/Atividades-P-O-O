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
    linha = arquivo.read()
    for palavra in linha.split():
        if palavra in quant_palavras:
            quant_palavras[palavra] += 1
        else:
            quant_palavras[palavra] = 1
ordenado = sorted(quant_palavras.items(), key=lambda item: item[1], reverse=True)
print(ordenado)



#Questao_03
def mesclar_dicionarios(dict_1, dict_2):
    dict_3 = {}
    for chave, valor in dict_1.items():
        dict_3[chave] = valor
        for chave, valor in dict_2.items():
            if chave not in dict_3:
                dict_3[chave] = valor
            else:
                if dict_3[chave] > dict_2[chave]:
                    dict_3[chave] = dict_3[chave]
                elif dict_2[chave] > dict_3[chave]:
                    dict_3[chave] = dict_2[chave]
    return dict_3
dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

#Questao_04
def filtrar_dicionario(dados, chaves_filtradas):
    dicionario_final = {}
    for chave in chaves_filtradas:
        if chave in dados:
            dicionario_final[chave] = dados[chave]
    return dicionario_final
dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

#Questao_05
def resultado_votacao(votos):
    resultado = {}
    totais = {}
    for sessao in votos:
        for candidato, quantidade in sessao.items():
            if candidato in totais:
                totais[candidato] += quantidade
            else:
                totais[candidato] = quantidade
        total_geral = 0
        for voto in totais.values():
            total_geral += voto
        for chave, valor in totais.items():
            percentual = valor / total_geral * 100, 2
            resultado[chave] = (totais[chave], percentual)
    return resultado

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)
    