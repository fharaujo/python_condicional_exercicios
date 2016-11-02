"""
Faça um programa que peça a velocidade do carro. Caso o carro ultrapasse a velocidade de 60 km/h,
exiba uma mensagem que o cidadão foi multado e exiba o valor da multa, cobrando R$ 6,00 para cada
km que ultrapasse o limite de 60 km/h
"""

velocidade = int(input("Velocidade do carro: "))

if velocidade <= 60:
    print("Você não foi multado!")
elif velocidade > 60:
    multa = 6
    km_acima = velocidade - 60
    valor = km_acima * multa
    print("Você foi multado e o valor da multa é R$", valor)
else:
    print("Digite o valor para km válido!")