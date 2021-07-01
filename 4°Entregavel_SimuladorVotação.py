# Projeto 04 - Simulador de votação:

# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:

# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):

# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação

import os
from datetime import datetime


os.system('cls')

# Lista aninhada criada para guardar a infomação dos candidatos , votos nulos e em branco
votação = [['candidato1', 0], ['candidato2', 0], [
    'candidato3', 0], ['Votos nulos', 0], ['Votos Brancos', 0]]


class Votacao:  # Criação da Class Votacao
    # primeira função inicia sozinha pegandos as informações de nome e idade
    def __init__(self, nome, idade):
        self.nomePessoa = nome
        self.idadeIdade = idade

    # segunda função tem o dever de averiguar se a pessoa pode ou não votar
    def autoriza_voto(self):
        if self.idadeIdade == 16 or self.idadeIdade == 17 or self.idadeIdade > 65:
            return f'''{self.nomePessoa} você tem {self.idadeIdade} anos 
                      Você tem direito ao voto opcional!!!!
                      '''
        # elif self.idadeIdade <= 15:
        #     return f'''{self.nomePessoa} você tem {self.idadeIdade} anos
        #               Você não direito ao voto!!!
        #               '''
        else:
            return f'''{self.nomePessoa} você tem {self.idadeIdade} anos 
                      Você é obrigado a votar!!!!
                      '''

    def votacao(self, voto):  # terceira função tem a tarefa de perguntar ao usuario qual será seu voto, caso ele tenha mais que 15 anos
        if self.idadeIdade <= 15:
            return '''{self.nomePessoa} você tem {self.idadeIdade} anos 
                      Você não direito ao voto!!!'''
        else:
            if voto == 1:
                votação[0][1] += 1
            elif voto == 2:
                votação[1][1] += 1
            elif voto == 3:
                votação[2][1] += 1
            elif voto == 5:
                votação[4][1] += 1
            else:
                votação[3][1] += 1


while True:  # While criado para perguntado para o usuario caso ele queira continuar a votar
    pessoa = Votacao(
        nome='Dorival',
        #str(input("Qual o seu nome?: ")),
        # int(input("Qual o ano do seu nascimento e apenas o ano do nascimento: "))
        idade=datetime.now().year - 1996
    )
    print(pessoa.autoriza_voto())

    pessoa.votacao(int(input(
        '''        Digite o numero corespondente ao seu candidato
                                [1] Candidato 1
                                [2] Candidato 2
                                [3] Candidato 3
                                [4] Voto nulo
                                [5] Voto em Branco
        '''
    )))
    print(votação)

    parar = str(input("Você deseja continuar [S/N]: ")).upper()
    if parar.startswith('N'):
        os.system('cls')
        break

while True:
    os.system('cls')
    # Função MAX usado para saber qual o maior valor dentro da Lista votação, mas ha um problema ,caso tenha um empate , ele só vai pegar o primeiro
    Candidatoeleito, votoEleito = max(votação, key=lambda item: item[1])
    print(f'''
                    Após as votações, 
                
            O cadidato 1    recebeu {votação[0][1]} Votos
            O cadidato 2    recebeu {votação[1][1]} Votos
            O cadidato 3    recebeu {votação[2][1]} Votos
            Votos nulos     recebeu {votação[4][1]} Votos
            Votos brancos   recebeu {votação[3][1]} Votos
           
            O candidato eleito foi {Candidatoeleito} 
            Com {votoEleito} Votos.
        
        
        ''')
    break
