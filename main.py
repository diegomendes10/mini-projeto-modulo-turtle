from turtle import Turtle

# t = Turtle()  inicializa uma Turtle
# t.speed()  define a velocidade
# t.forward()  movimenta para frente
# t.right()  rotaciona para direita
# t.left()  rotaciona para esquerda
# t.backward()  movimenta para trás

t = Turtle()

while True:
    movimento = input('Entre com uma das opção abaixo: \n\n'
                      'letra "W" para movimentar para FRENTE \n'
                      'letra "S" para movimentar para TRÁS \n'
                      'letra "D" para virar para DIREITA \n'
                      'letra "A" para virar para ESQUERDA \n'
                      'letra "Z" para SAIR do jogo \n'
                      'O que você deseja fazer? \n ').upper()

    if movimento == 'A':
        virar_para_esquerda = int(input('Quantos graus?'))
        t.left(virar_para_esquerda)
    elif movimento == 'D':
        virar_para_direita = int(input('Quantos graus? '))
        t.right(virar_para_direita)
    elif movimento == 'W':
        mover_para_frente = int(input('Quantos pixels? '))
        velocidade = int(input('Qual a velocidade? '))
        t.forward(mover_para_frente)
        t.speed(velocidade)
    elif movimento == 'S':
        mover_para_tras = int(input('Quantos pixels? '))
        velocidade = int(input('Qual a velocidade? '))
        t.backward(mover_para_tras)
        t.speed(velocidade)
    elif movimento == 'Z':
        print('O mini game foi finalizado.')
        break

    else:
        print('Opção inválida.')
