altura=float(input("Digite sua altura: "))
peso=float(input("Digite o seu peso: "))
print(f"A altura registrada é de :{altura} m")
print(f"O peso registrado é de :{peso} Kgs")
imc=peso/(altura*altura)
print(f"Valor do imc:{imc}")
if (imc>18.5 and imc<25.0):
    print("Peso normal!")
elif(imc>25.0):
    print("Sobrepeso!")
elif(imc<18.5):
    print("Abaixo do peso!")