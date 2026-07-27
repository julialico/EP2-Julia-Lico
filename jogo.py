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

def leentrada(mensagem):
    entrada = input(mensagem)
    entrada = entrada.strip().upper()
    return entrada
 
 
def jogapartida(basepornivel):
    nome = input('Qual é o seu nome? ').strip()
    if nome == '':
        nome = 'Jogador'
 
    tela.exibemanual()
 
    premioatual = 0
    pulosrestantes = PULOSINICIAIS
    ajudasrestantes = AJUDASINICIAIS
    sorteadas = []
    indice = 0
 
    while indice < len(PREMIOS):
        nivel = FAIXAS[indice]
        questao = sorteia_questao_inedita(basepornivel, nivel, sorteadas)
        ajudausada = False
        continuapergunta = True
 
        while continuapergunta:
            tela.exibeestado(nome, premioatual, pulosrestantes, ajudasrestantes)
            print(questao_para_texto(questao, indice + 1))
 
            entrada = leentrada('Escolha A, B, C, D, PULA ou AJUDA: ')
 
            if entrada not in OPCOESVALIDAS:
                tela.escreveerro('Opcao invalida! Digite A, B, C, D, PULA ou AJUDA.')
 
            elif entrada == 'PULA':
                if pulosrestantes > 0:
                    pulosrestantes = pulosrestantes - 1
                    questao = sorteia_questao_inedita(basepornivel, nivel, sorteadas)
                    ajudausada = False
                    tela.escreveaviso('Pergunta trocada! Pulos restantes: ' + str(pulosrestantes))
                else:
                    tela.escreveerro('Voce nao tem mais pulos disponiveis!')
 
            elif entrada == 'AJUDA':
                if ajudausada:
                    tela.escreveerro('Voce ja usou ajuda nesta pergunta, nao pode usar de novo!')
                elif ajudasrestantes <= 0:
                    tela.escreveerro('Voce nao tem mais ajudas disponiveis!')
                else:
                    ajudasrestantes -= 1
                    ajudausada = True
                    tela.escreveinfo(gera_ajuda(questao))
 
            elif entrada == questao['correta']:
                premioatual = PREMIOS[indice]
                tela.escrevesucesso('Resposta correta!')
                tela.escrevepremio(premioatual)
 
                if premioatual == PREMIOS[-1]:
                    tela.escrevesucesso('PARABENS ' + nome + '! Voce ganhou o premio maximo!')
                    return premioatual
 
                quer = leentrada('Deseja PARAR e sair com o premio, ou CONTINUAR jogando? (PARAR/CONTINUAR): ')
                if quer == 'PARAR':
                    tela.escrevesucesso(nome + ', voce saiu do jogo com R$ ' + tela.formatamoeda(premioatual) + '!')
                    return premioatual
                else:
                    indice = indice + 1
                    continuapergunta = False
 
            else:
                tela.escreveerro('Resposta errada! A alternativa correta era: ' + questao['correta'])
                tela.escreveerro(nome + ', voce perdeu tudo e sai sem nenhum premio!')
                return 0
 
    return premioatual

def main():
    if not baseconsistente(quest):
        tela.escreveerro('A base de perguntas esta inconsistente. Corrija antes de jogar.')
        return
 
    basepornivel = transforma_base(quest)
 
    jogarnovamente = True
    while jogarnovamente:
        jogapartida(basepornivel)
        resposta = leentrada('Deseja jogar novamente? (SIM/NAO): ')
        jogarnovamente = (resposta == 'SIM')
 
    tela.escreveinfo('Obrigado por jogar o Jogo da Fortuna DesSoft!')
 
 
main()