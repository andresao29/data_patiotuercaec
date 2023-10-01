from autos_dat import get_price

marcas = ["kia", "chevrolet", "ford"]

for t in marcas:
    get_price(marca=t, verbose=True)
