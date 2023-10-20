areaPintada=float(input("Tamanho da area a ser pintada em metros quadrados: "))
litrosNecessarios=(1/3)*areaPintada
latasNecessarias=(litrosNecessarios//18)+1
print(f"A area a ser pintada tem: {areaPintada} metros quadrados.")
print(f"Serão necessarios: {litrosNecessarios} litros de tinta")
print(f"serão necessarias: {latasNecessarias} latas de tinta")