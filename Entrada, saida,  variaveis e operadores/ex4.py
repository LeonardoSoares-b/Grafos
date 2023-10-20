valorHora=float(input("Valor da hora trabalhada: "))
horasTrabalhadas=float(input("Horas trabalhadasno mes: "))
salarioBruto=valorHora*horasTrabalhadas
print(f"O salario bruto é de : {salarioBruto}")
impostoRenda=salarioBruto*0.15
print(f"O valor pago em imposto de renda é de: {impostoRenda}")
inss=salarioBruto*0.10
print(f"O valor destinado ao INSS é de: {inss}")
sind=salarioBruto*0.02
print(f"O valor pago ao sindicato é de: {sind}")
descontos=impostoRenda+inss+sind
salarioLiquido=salarioBruto-descontos
print(f"O salario liquido é de: {salarioLiquido}")