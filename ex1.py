#receba a informação do nome de uma pessoa e escreva na tela "ola pessoa"
nome = input("Digite seu nome: ")
print(f"ola {nome}")

#altura e largura retangulo
altura = input("Digite a altura do retangulo: ")
largura = input("Digite a largura do retangulo: ")
print("a area do retangulo é: ")
print(float(altura)*float(largura))

#raio do circulo e calcule a area do circulo 
pi=3.14
R=input("digite o raio do circulo: ")
print("a area do circulo é: ")
print(float(pi)*float(R)**2)

#converta celsius para fahrenheit F=C*1.8+32
C=input("digite a temperatura em celsius: ")
F=(float(C)*1.8+32)
print(F)

#converta fahrenheit para celsius C=(F-32)*5/9
F=input("digite um numero em Fahrenheit: ")
C=((float(F)-32)*5/9)
print(round(C,2))


