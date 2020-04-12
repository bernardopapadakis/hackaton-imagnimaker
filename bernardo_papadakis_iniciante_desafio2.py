from random import choice
from time import sleep

# Título
print('-'*40)
print('{:^40}'.format(' PEDRA, PAPEL E TESOURA '))
print('-'*40)

# Declaração das variáveis

# Variável das rodadas
r = 0
# Variável dos Pontos do Jogador
pj = 0
# Variável dos pontos do Computador
pc = 0

# Entrada do nome do jogador
nome = str(input('\033[mDigite o seu nome: ')).capitalize()

# Inicia o loop
while True:
    # Se a variável das rodadas for diferente de 5
    if r != 5:
        print('-' * 40)
        # Entrada da jogada do jogador
        j = str(input('Escolha sua jogada [PEDRA/PAPEL/TESOURA]\nSua resposta: ')).lower()
        # Jogada do computador
        c = choice(['pedra', 'papel', 'tesoura'])
        # Se jogador ganhar
        if j == 'pedra' and c == 'tesoura' or j == 'papel' and c == 'pedra' or j == 'tesoura' and c == 'papel':
            # Simulação da "musiquinha" que cantam ao jogar pedra, papel e tesoura
            print('PEDRA', end='')
            sleep(0.5)
            print(', PAPEL', end=' ')
            sleep(0.5)
            print('e TESOURA!!!')
            sleep(0.5)
            # Placar
            print(f'{nome} \033[1:34m{j}\033[m X \033[1:31m{c}\033[m Computador')
            # Mensagem de vitória
            print('\033[1:34mVOCÊ GANHOU!\033[m\n')
            # Para contar o ponto do Jogador
            pj += 1
            # Para contar a rodada
            r += 1
        # Se der empate
        elif j == 'pedra' and c == 'pedra' or j == 'papel' and c == 'papel' or j == 'tesoura' and c == 'tesoura':
            # Simulação da "musiquinha" que cantam ao jogar pedra, papel e tesoura
            print('PEDRA', end='')
            sleep(0.5)
            print(', PAPEL', end=' ')
            sleep(0.5)
            print('e TESOURA!!!')
            sleep(0.5)
            # Placar
            print(f'{nome} \033[1:33m{j}\033[m X \033[1:33m{c} \033[mComputador')
            # Mensagem de empate
            print('\033[1:33mEMPATE!\033[m\n')
            # Contando os pontos do jogador e do computador
            pj += 1
            pc += 1
            # Contando a rodada
            r += 1
        # Se jogador perder
        elif j == 'pedra' and c == 'papel' or j == 'papel' and c == 'tesoura' or j == 'tesoura' and c == 'pedra':
            # Simulação da "musiquinha" que cantam ao jogar pedra, papel e tesoura
            print('PEDRA', end='')
            sleep(0.5)
            print(', PAPEL', end=' ')
            sleep(0.5)
            print('e TESOURA!!!')
            sleep(0.5)
            # Placar
            print(f'{nome} \033[1:31m{j}\033[m X \033[1:34m{c}\033[m Computador')
            # Mensagem de derrota
            print('\033[1:31mVOCÊ PERDEU!\033[m\n')
            # Contando o ponto do computador
            pc += 1
            # Contando a rodada
            r += 1
        # Se a jogada do jogador for inválida
        else:
            print('\033[31mResposta inválida! Tente novamente.\033[m\n')


    else:# Caso as 5 rodadas já tenham acontecido
        print('-' * 40)
        # Pergunta se o jogador deseja continuar ou não
        sn = str(input(f'\n{nome}, você deseja continuar?\nSua resposta: [\033[1:34mS\033[m/\033[1:31mN\033[m] ')).upper()
        # Se o jogador quiser continuar a jogar
        if sn == 'S':
            # Reseta a variável das rodadas
            r = 0
        # Se o jogador não mais quiser jogar
        elif sn == 'N':
            # Se os pontos do jogador for maior do que os pontos do computador
            if pj > pc:
                # Placar
                print(f'{nome} \033[1:34m{pj}\033[m X \033[1:31m{pc}\033[m Computador')
                # Mensagem dizendo ao jogador que ele venceu
                print('\033[1:34mVOCÊ GANHOU!\033[m')
            # Se os pontos do jogador for menor do que os pontos do computador:
            elif pj > pc:
                # Placar
                print(f'{nome} \033[1:31m{pj}\033[m X \033[1:34m{pc}r\033[m Computado')
                # Mensagem dizendo ao jogador que ele perdeu
                print('\033[1:31mVOCÊ PERDEU!\033[m')
            # Se os dois empatarem
            else:
                # Placar
                print(f'{nome} \033[1:33m{pj}\033[m X \033[1:33m{pc}\033[m Computador')
                # Mensagem de empate
                print('\033[1:33mEMPATE!\033[m')
            # Encerra o loop
            break
        else:
            print('\033[31mResposta inválida! tente novamente.\033[m')# Mensagem de resposta inválida
