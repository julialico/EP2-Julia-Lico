from funcoes import (transforma_base, valida_questao, valida_questoes,
                          sorteia_questao, sorteia_questao_inedita,
                          questao_para_texto, gera_ajuda)
from baseperguntas import quest
import tela
 
PREMIOS = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
FAIXAS = ['facil', 'facil', 'facil', 'medio', 'medio', 'medio', 'dificil', 'dificil', 'dificil']
 
PULOSINICIAIS = 3
AJUDASINICIAIS = 2
 
OPCOESVALIDAS = ['A', 'B', 'C', 'D', 'PULA', 'AJUDA']
 
 
def baseconsistente(lista):
    erros = valida_questoes(lista)
    temerro = False
    for indice in range(len(erros)):
        if len(erros[indice]) > 0:
            temerro = True
            tela.escreveerro('Pergunta ' + str(indice) + ' com problema: ' + str(erros[indice]))
 
    pornivel = transforma_base(lista)
    for nivel in ['facil', 'medio', 'dificil']:
        if nivel not in pornivel:
            temerro = True
            tela.escreveerro('Nao existe nenhuma pergunta de nivel "' + nivel + '" na base!')
        elif len(pornivel[nivel]) < 3:
            temerro = True
            tela.escreveerro('É preciso ter pelo menos 3 perguntas de nivel "' + nivel + '" na base!')
 
    return not temerro
