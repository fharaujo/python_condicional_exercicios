""""
Crie um programa que calcule o Imposot de Renda pela faixa salarial, sabendo que os salários até
R$ 1.000 reais não pagam Imposto, ou seja, 0 % de aliquota. Salários entre R$ 1.000 e R$ 3.000
pagam Imposto de 20 % de aliquota e os salários acima de R$ 3.000, pagam  35 % de aliquota.
"""

salario = float(input("Digite seu salário: "))

if salario < 1000:
    imposto = 0
    valor = (salario * imposto)
elif salario >=1000 and salario <= 3000:
    imposto = 0.20
    valor = (salario * imposto)
else:
    imposto = 0.35
    valor = (salario * imposto)

total = salario - valor

print("O salário de R$ %.2f, terá um desconto de imposto de %.2f e o valor líquido: R$ %.2f" % (salario, valor, total))