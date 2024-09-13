peso = float(input("digite seu peso em kg: "))
altura = float(input("digite sua altura em metros: "))
IMC= peso/altura**2
print(f"seu IMC é {IMC:.2f}")

if IMC<18.5:
    print("Você está no peso abaixo do ideal, com magreza.")

elif IMC<=24.9:
    print("Você está no peso ideal.") 

elif IMC<=29.9:
    print("Você está com sobrepeso.")

elif IMC<=34.9:
    print("Você está com obesidade grau I.")

elif IMC<=39.9:
    print("Você está com obesidade grau II.")

else:
    print("Você está com obesidade grau III.")

