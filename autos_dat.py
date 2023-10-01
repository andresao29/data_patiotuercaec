import requests

from mongodb import client


def get_price(marca: str, verbose: bool = False) -> dict:
    url = f"https://ecuador.patiotuerca.com/ptx/api/v2/nitros?type=autos&brand={marca}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()

    precio = r['data']['result_set'][0]['PriceValue']
    marca = r['data']['result_set'][0]['BrandValue']
    anio = r['data']['result_set'][0]['YearValue']
    ciudad = r['data']['result_set'][0]['CityValue']
    modelo = r['data']['result_set'][0]['ModelValue']

    # precio1 = r['data']['result_set'][1]['PriceValue']
    # marca1 = r['data']['result_set'][1]['BrandValue']
    # anio1 = r['data']['result_set'][1]['YearValue']
    # ciudad1 = r['data']['result_set'][1]['CityValue']
    # modelo1 = r['data']['result_set'][1]['ModelValue']
    #
    # precio2 = r['data']['result_set'][2]['PriceValue']
    # marca2 = r['data']['result_set'][2]['BrandValue']
    # anio2 = r['data']['result_set'][2]['YearValue']
    # ciudad2 = r['data']['result_set'][2]['CityValue']
    # modelo2 = r['data']['result_set'][2]['ModelValue']
    #
    # precio3 = r['data']['result_set'][3]['PriceValue']
    # marca3 = r['data']['result_set'][3]['BrandValue']
    # anio3 = r['data']['result_set'][3]['YearValue']
    # ciudad3 = r['data']['result_set'][3]['CityValue']
    # modelo3 = r['data']['result_set'][3]['ModelValue']
    #
    # precio4 = r['data']['result_set'][4]['PriceValue']
    # marca4 = r['data']['result_set'][4]['BrandValue']
    # anio4 = r['data']['result_set'][4]['YearValue']
    # ciudad4 = r['data']['result_set'][4]['CityValue']
    # modelo4 = r['data']['result_set'][4]['ModelValue']

    if verbose:
        print(f"{ciudad} {marca} {modelo} {anio} {precio}")
        # print(f"{ciudad1} {marca1} {modelo1} {anio1} {precio1}")
        # print(f"{ciudad2} {marca2} {modelo2} {anio2} {precio2}")
        # print(f"{ciudad3} {marca3} {modelo3} {anio3} {precio3}")
        # print(f"{ciudad4} {marca4} {modelo4} {anio4} {precio4}")
    return {
        "ciudad": ciudad,
        "marca": marca,
        "modelo": modelo,
        "anio": anio,
        "precio": precio
    }


def set_price(document: dict):
    _ = client.get_database('marcas').get_collection('Andres').insert_one(document=document)
    return 'ok'
