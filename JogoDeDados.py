# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer;
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.

from random import randint
from time import sleep
import operator

aposta = list()

jogador1 = jogador2 = jogador3 = jogador4 = int(0)
empates = int(1)
rodadas = int(input("Quantas rodadas você ira querer jogar? : "))
sleep(2)
for contador in range(1, rodadas + 1):
    lAposta = dict()
    situacao = ''
    lAposta['jogador1'] = randint(1, 7)
    lAposta['jogador2'] = randint(1, 7)
    lAposta['jogador3'] = randint(1, 7)
    lAposta['jogador4'] = randint(1, 7)
    # Condicional criada para determinar o ganhador da rodada
    if lAposta['jogador2'] < lAposta['jogador1'] > lAposta['jogador3'] and lAposta['jogador1'] > lAposta['jogador4']:
        situacao = 'jogador1'
        jogador1 += 1
    elif lAposta['jogador1'] < lAposta['jogador2'] > lAposta['jogador3'] and lAposta['jogador2'] > lAposta['jogador4']:
        situacao = 'jogador 2'
        jogador2 += 1
    elif lAposta['jogador1'] < lAposta['jogador3'] > lAposta['jogador2'] and lAposta['jogador3'] > lAposta['jogador4']:
        situacao = 'jogador 3'
        jogador3 += 1
    elif lAposta['jogador1'] < lAposta['jogador4'] > lAposta['jogador2'] and lAposta['jogador4'] > lAposta['jogador3']:
        situacao = 'jogador 4'
        jogador4 += 1
    else:
        situacao = 'Empate'
    # Essa variavel serve para determinar a quantidade de empates
    empates = contador - (jogador1+jogador2+jogador3+jogador4)
    # Esse comando serve para ordernar o Dict em ordem crescente, com o uso do .itemgetter(), posso selecionar o item que vai ser ordenado
    sortedResult = sorted(
        lAposta.items(), key=operator.itemgetter(1), reverse=True)
    # Comando usado para criar uma copia do Dict em Uma Lista
    aposta.append(sortedResult)
    ###########################
    print(f'''
            O ganhador da rodada foi
                    {situacao}
                    {sorted(
        lAposta.items(), key=operator.itemgetter(1), reverse=True)}

    ''')
    sleep(1)

if jogador2 < jogador1 > jogador3 and jogador1 > jogador4:
    print(f'        O campeão foi o Jogador 1 com {jogador1} Vitorias')
elif jogador1 < jogador2 > jogador3 and jogador2 > jogador4:
    print(f'        O campeão foi o Jogador 2 com {jogador2} Vitorias')
elif jogador1 < jogador3 > jogador2 and jogador3 > jogador4:
    print(f'        O campeão foi o Jogador 3 com {jogador3} Vitorias')
elif jogador1 < jogador4 > jogador2 and jogador4 > jogador3:
    print(f'        O campeão foi o Jogador 4 com {jogador4} Vitorias')
else:
    print("         Não houve campeão, o resultado terminou em empate")
