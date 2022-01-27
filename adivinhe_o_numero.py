"""

Jogo de adivinhação de numero

O computador "pensará" em um número, então
o usúario terá que adivinhar qual será.

"""
from random import randint

qtd_jogadores = 2

numero_secreto = randint(1,10)

tentativas = [3, 3]

venceu = False

vencedor = 0

contador = 1

fim_tentativas = 0

começar = input("Clique em quanquer tecla para começão")

if começar != None:
    print("Bem-vindos, o computador acaba de pensar em um número de 1 a 10"
        "\nTente adivinhar qual é:")

    while(fim_tentativas != 2):
        
        if contador%2 != 0 and tentativas[0] > 0:
            print(f"Você tem \033[34m{tentativas[0]}\033[0;0m tentativas.")
            valor = input("Chute um número: ")
            try:
                valor = int(valor)

                if valor == numero_secreto:
                    venceu = True
                    vencedor = 1
                    break

                if tentativas[0] > 0:
                    tentativas[0] -= 1
                
                if tentativas[0] == 0 and valor != numero_secreto:
                    print("Você excedeu seu número de tentativas.")
                    fim_tentativas += 1
            except Exception as e:
                print("Erro:", e)

        elif contador%2 == 0 and tentativas[1] > 0:
            print(f"Você tem \033[32m{tentativas[1]}\033[0;0m tentativas.")
            valor = input("Chute um número: ")

            try:
                valor = int(valor)

                if valor == numero_secreto:
                    venceu = True
                    vencedor = 2
                    break
                
                if tentativas[1] > 0:
                    tentativas[1] -= 1
                
                if tentativas[0] == 0 and valor != numero_secreto:
                    print("Você excedeu seu número de tentativas.")
                    fim_tentativas += 1
            except Exception as e:
                print("Erro:", e)

        contador += 1


if venceu:
    print(f"\nParabéns, jogador {vencedor}. Você venceu.")
    print(f"O valor que o computador pensou era {numero_secreto}.")

else:
    print("\nNão houve vencedor nesta partida.")
    print(f"O número que o computador pensou foi {numero_secreto}")
    

