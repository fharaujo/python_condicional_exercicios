"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""



letra = input("Digite uma letra e o computador dirá se é Vogal ou Consoante: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Letra '%s' é uma vogal" % letra )
elif letra == "":
    print("Digite uma letra!")
else:
    print("Letra '%s' é uma consoante" % letra)
