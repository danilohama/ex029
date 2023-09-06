"""Escreva um programa que leia a velocidade de um carro.
> Se ele ultrapassar a velocidade de 80KM/H Mostre uma mensagem que dizendo que ele foi multado.
> A multa vai custar R$7,00 por cada KM acima do limite
"""
#  Estrutura condicinal SIMPLES, pois só tem um "IF"
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print(' \033[0:31m MULTADO! Você excedeu o limite permitido que é de 80km/h\033[0:0m')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')
