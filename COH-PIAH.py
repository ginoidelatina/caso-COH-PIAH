import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.\n")

    tamMedPalavra = float(input("Entre o tamanho medio de palavra: "))
    typeToken = float(input("Entre a relação Type-Token: "))
    hapaxLegomana = float(input("Entre a Razão Hapax Legomana: "))
    tamMedSentenca = float(input("Entre o tamanho médio de sentença: "))
    comMedSentenca = float(input("Entre a complexidade média da sentença: "))
    tamMedFrase = float(input("Entre o tamanho medio de frase: "))

    print()

    return [tamMedPalavra, typeToken, hapaxLegomana, tamMedSentenca, comMedSentenca, tamMedFrase]

def le_textos():  # Função que recebe os textos.
    '''A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")  # + str(1) + Pesquise
    while texto:
        textos.append(texto)
        i += 1  # Seria o contador da quantidade de textos?
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentenças dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentença e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):  # Razão Hapax Legomana
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):  # Relação Type-Token
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)  
    numSentencas = 0
    somaCarSentencas = 0
    frases = []     
    for i in range(len(sentencas)):
        numSentencas += 1
        lista_FrasesSentenca = separa_frases(sentencas[i])  
        frases.append(lista_FrasesSentenca)
        somaCarSentencas = somaCarSentencas + len(sentencas[i])  

    numFrases = 0
    somaCarFrase = 0
    palavras = []
    for lin in range(len(frases)):
        for col in range(len(frases[lin])):     
            numFrases += 1
            palavrasFrase = separa_palavras(frases[lin][col])
            palavras.append(palavrasFrase)
            somaCarFrase += len(frases[lin][col])

    matrizPalavras = []
    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            matrizPalavras.append(palavras[linha][coluna])
    palavras = matrizPalavras[:]

    totalPalavras = len(palavras)

    
    tamanhoPalavras = 0
    for l in range(len(palavras)):
        for c in range(len(palavras[l])):
            tamanhoPalavras += len(str(palavras[l][c]))

    tamMedPalavras = tamanhoPalavras / totalPalavras
    type_token = n_palavras_diferentes(palavras) / totalPalavras
    hapax_legomana = n_palavras_unicas(palavras) / totalPalavras
    tamMedioSentenca = somaCarSentencas / numSentencas
    complexSentenca = numFrases / numSentencas
    tamMedioFrase = somaCarFrase / numFrases
    return [tamMedPalavras, type_token, hapax_legomana, tamMedioSentenca, complexSentenca, tamMedioFrase]  

def compara_assinatura(ass_a, ass_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    numerador = sum(abs(a - b) for a, b in zip(ass_a, ass_b))  
    simi = ( numerador / 6 )  
    return simi  

def avalia_textos(listaTextos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    textos = listaTextos
    listaAssinaturas = []
    for i in range(len(textos)):
        listaAssinaturas.append(calcula_assinatura(textos[i]))  

    similiaridades = []
    for i in range(len(listaAssinaturas)):
        simi = listaAssinaturas[i]
        xsimi = compara_assinatura(simi, ass_cp)
        similiaridades.append(xsimi)

    menor = similiaridades[0]  
    for c in range(len(similiaridades)):  
        if similiaridades[c] < menor:
            menor = similiaridades[c]
            position = c + 1  
    return position

def main():
    ass_cp = le_assinatura()  
    listaTextos = le_textos()  

    return print("O autor do texto ", avalia_textos(listaTextos, ass_cp), " está infectado com COH-PIAH")
