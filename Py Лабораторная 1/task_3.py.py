V_1disk = 1.44 * 1024 * 1024
V_nasymbol = 4
Stranizi = 100
Stroky = 50
Symbols = 25

V_knigi = Stranizi * Stroky * Symbols
V_naknigy = V_nasymbol * V_knigi

book = int(V_1disk // V_naknigy)

print("Количество книг, помещающихся на дискету:", book)