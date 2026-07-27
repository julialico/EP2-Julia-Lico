def transforma_base (lista):
    final = {}
    for questao in lista:
        nivel = questao['nivel']
        if nivel not in final:
            final[nivel] = [questao]
        else:
            final[nivel].append(questao)
    return final


def valida_questao(questao):
    retorno = {}

    if 'titulo' not in questao:
        retorno['titulo'] = 'nao_encontrado'
    elif questao['titulo'].strip() == '':
        retorno['titulo'] = 'vazio'

    niveis = ['facil', 'medio', 'dificil']
    if 'nivel' not in questao:
        retorno['nivel'] = 'nao_encontrado'
    elif questao['nivel'] not in niveis:
        retorno['nivel'] = 'valor_errado'

    validas = 'ABCD'
    if 'opcoes' not in questao:
        retorno['opcoes'] = 'nao_encontrado'
    elif len(questao['opcoes']) != 4:
        retorno['opcoes'] = 'tamanho_invalido'
    else:
        opcoes = questao['opcoes']
        if 'A' not in opcoes.keys():
            retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        elif 'B' not in opcoes.keys():
            retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        elif 'C' not in opcoes.keys():
            retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        elif 'D' not in opcoes.keys():
            retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        else:
            for opcao, resposta in opcoes.items():
                if resposta.strip() == '':
                    if 'opcoes' not in retorno:
                        retorno['opcoes'] = {}
                    retorno['opcoes'][opcao] = 'vazia'

    if 'correta' not in questao:
        retorno['correta'] = 'nao_encontrado'
    elif questao['correta'] not in validas:
        retorno['correta'] = 'valor_errado'
        
    if len(questao) != 4:
        retorno['outro'] = 'numero_chaves_invalido'
    
    return retorno


def valida_questoes(lista):
    final = []
    for questao in lista:
        erros = valida_questao(questao)
        final.append(erros)
    return final


import random
def sorteia_questao(questoes, nivel):
    listanivel = questoes[nivel]
    sorteada = random.choice(listanivel)
    return sorteada


def sorteia_questao_inedita(questoes, nivel, sorteadas):
    sorteada = sorteia_questao(questoes, nivel)

    while sorteada in sorteadas:
        sorteada = sorteia_questao(questoes, nivel)

    sorteadas.append(sorteada)
    
    return sorteada


def questao_para_texto(questao, id):
    texto = '----------------------------------------' + "\n"
    texto = texto + "QUESTAO " + str(id) + "\n\n"

    texto = texto + questao["titulo"] + "\n\n"

    texto = texto + "RESPOSTAS:\n"

    for letra in questao["opcoes"]:
        texto = texto + letra + ": " + questao["opcoes"][letra] + "\n"

    return texto


import random
def gera_ajuda(questao):
    erradas = []
    for letra in questao["opcoes"]:
        if letra != questao["correta"]:
            erradas.append(questao["opcoes"][letra])

    qtde = random.randint(1, 2)

    sorteadas = []
    while len(sorteadas) < qtde:
        indice = random.randint(0, (len(erradas) - 1))
        if indice not in sorteadas:
            sorteadas.append(indice)

    texto = "DICA:\n" + "Opções certamente erradas: " + erradas[sorteadas[0]]
    if qtde == 2:
        texto = texto + " | " + erradas[sorteadas[1]]

    return texto