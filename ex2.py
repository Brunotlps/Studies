"""
Um posto está vendendo combustíveis com a 
seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de 
litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, 
G-gasolina), calcule e imprima o valor a ser 
pago pelo cliente sabendo-se que o preço do 
litro da gasolina é R$ 2,50 o preço do litro 
do álcool é R$ 1,90.
"""

tipo = str(input('Digite o tipo de combustível sendo: \nA - Álcool e G - Gasolina: ')).upper()

if tipo == 'A':
    litros = float(input('Quantos litros de álcool deseja? '))
    p = litros * 1.90
    if litros <= 20:
        pn =  p - ((p * 3) / 100)
        print(f'Valor bruto R$ {p}\nValor com desconto R$ {pn}')  
    else:
        pn = p - ((p * 5) / 100)
        print(f'Valor bruto R$ {p}\nValor com desconto R$ {pn}')
if tipo == 'G':
    litros = float(input('Quantos litros de gasolina deseja? '))
    p = litros * 2.50
    if litros <= 20:
        pn = p - ((p * 4) / 100)
        print(f'Valor bruto R$ {p}\nValor com desconto R$ {pn}')
    else:
        pn = p - ((p * 6) / 100)
        print(f'Valor bruto R$ {p}\nValor com desconto R$ {pn}')