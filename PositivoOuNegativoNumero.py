"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

numero = int(input("Digite um valor inteiro: "))

if numero > 0:
    print(" %i é um número positvo" % numero)
elif numero == 0:
    print(" %i é nulo" % numero)
else:
    print(" %i é valor negativo" % numero)