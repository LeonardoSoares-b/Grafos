tamanhoMb=float(input("tamanho do arquivo em MB: "))
velocidade=float(input("Velocidade em Mbps: "))
tempo=(tamanhoMb/velocidade)/60
print(f"Arquivo de tamanho: {tamanhoMb} Mb")
print(f"Velocidade de {velocidade} Mbps")
print(f"Tempo de {tempo:.2f} minutos")