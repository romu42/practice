# https://codechalleng.es/bites/180/

from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    for line in data.split('\n'):
        last_name, first_name, country = line.split(',')
        countries[country].append(f"{first_name} {last_name}")
    countries.pop('country_code', None)
    return countries
if __name__ == '__main__':
    group_names_by_country(data)
