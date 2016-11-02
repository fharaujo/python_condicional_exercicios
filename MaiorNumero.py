"""Faça um Programa que peça dois números e imprima o maior deles."""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O %i é maior %i" %(numero1,numero2))
elif numero2 > numero1:
    print("O %i é maior %i" % (numero2, numero1))
else:
    print("Números são iguais!")
