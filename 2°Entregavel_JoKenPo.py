# Projeto 02 – Jogo Jokenpô
# Utilizando os conceitos aprendidos até estruturas de repetição, crie um programa que jogue pedra, papel e tesoura (Jokenpô) com você. O programa tem que:

# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha de quantidade de rodadas, se não finalize o programa.

from random import randint
from time import sleep
import os
# Variaveis que serão usadas para compor o código
itens = ("Papel", "Pedra", "Tesoura")
computador = randint(0, 2)
tentativas = int()

pergunta = int(
    input("Vamos jogar JO KE PO?, me diga quantas vezes você vai me desafiar ?: "))
sleep(1)
for c in range(pergunta):
    print("-=" * 12)
    jogador = int(input('''Qual você escolhe?\n
 [0]Papel\n
 [1]Pedra\n
 [2]Tesoura\n'''))
    print("-=" * 12)
    print(f"O computador escolheu {itens[computador]}")
    print(f"Você escolheu {itens[jogador]}")
    sleep(1)
    print("-=" * 12)
    # Aqui começa os If e Else, recebe o valor do Computador e compara com o valor Jogador(itens)

    if computador == 0:  # Se computador escolheu Papel
        if jogador == 0:  # Jogador escolheu Papel
            print("Empate")
        elif jogador == 1:  # Jogador escolheu Pedra
            print("Você perdeu!!!")
        elif jogador == 2:  # Jogador escolheu Tesoura
            print("Você ganhou !!!")
            tentativas += 1

    if computador == 1:  # Se computador escolheu Pedra
        if jogador == 0:  # Jogador escolheu Papel
            print("Você ganhou")
            tentativas += 1
        elif jogador == 1:  # Jogador escolheu Pedra
            print("Você empatou!!!")
        elif jogador == 2:  # Jogador escolheu Tesoura
            print("Você perdeu !!!")

    if computador == 2:  # Se computador escolheu Tesoura
        if jogador == 0:  # Jogador escolheu Papel
            print("Você Perdeu")
        elif jogador == 1:  # Jogador escolheu Pedra
            print("Você Ganhou!!!")
            tentativas += 1
        elif jogador == 2:  # Jogador escolheu Tesoura
            print("Você Empatou !!!")

    os.system("cls") or None  # O comando para limpar o terminal a cada lupping

print(f"Você ganhou {tentativas} Vezes!!")
