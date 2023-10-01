from autos_dat import get_price

marcas = ["kia", "chevrolet", "ford"]
ford ="ford"
renault="renault"

for t in marcas:
    get_price(marca=t, verbose=True)
