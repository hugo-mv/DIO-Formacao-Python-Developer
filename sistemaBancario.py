# Primeiro desafio do curso Desenvolvedor Python na plataforma DIO. Criando um sistema bancário com Python

from datetime import datetime

menu = '''
    Selecione a operação:

    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    operacao = input(menu)

    if operacao.lower() == 'd' or operacao.lower() =='depósito':
        try:
            deposito = float(input('Informe o valor do depósito: R$'))
        except:
            print('Erro. Valor em formato incorreto.')
        else:
            if deposito <= 0:
                    print('Erro. Valor de depósito deve ser um número positivo.')
            else:
                saldo += deposito
                extrato += (datetime.now().strftime("%d/%m/%Y %H:%M") + f' - Depósito: R${deposito:.2f}\n')
                print('Depósito realizado.')

    elif operacao.lower() == 's' or operacao.lower() =='saque':
        if numero_saques >= LIMITE_SAQUES:
            print('Você atingiu seu limite de saques diários.')
            continue
        
        try:
            saque = float(input('Informe o valor de saque: R$'))
        except:
            print('Erro. Valor em formato incorreto.')
        else:
            if saque > saldo:
                print('Você não tem saldo duficiente.')
            elif saque <= 0:
                print('Erro. Valor de saque deve ser um número positivo.')
            elif saque > limite:
                print('Valor ulrapassa seu limite de saque.')
            else:
                saldo -= saque
                extrato += (datetime.now().strftime("%d/%m/%Y %H:%M") + f' - Saque: R${saque:.2f}\n')
                numero_saques += 1
                print('Saque realizado.')

    elif operacao.lower() == 'e' or operacao.lower() =='extrato':
        print('------------- Extrato -------------')
        print(extrato)
        print(f'Saldo: {saldo:.2f}')
        print('-----------------------------------')

    elif operacao.lower() == 'q' or operacao.lower() == 'sair':
        print('Processo finalizado')
        break

    else:
        print(f'\"{operacao}\" é uma operação inválida. Selecione a operação desejada:')
