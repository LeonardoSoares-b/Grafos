g_dict= {"Ana":{"Bia":5, "Caio":4},
         "Bia":{"Ana":5, "Dida":2},
         "Caio":{"Dida":1},
         "Dida":{"Ana":4,"Bia":2,"Caio":1}}

try:
    weight=g_dict["Dida"]["Caio"]
    print(f"Dida e Caio são vizinhos")
except KeyError:
    print("Não vizinhos")
