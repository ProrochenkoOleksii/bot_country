import requests
import json
api_key = "RUZMRTZ2OXVkUjg2MjlXVnp0bG95WmpBM05laFlLY21sOEZJa283aA=="
headers = {"X-CSCAPI-KEY": api_key}


def country_info(my_country):
    if my_country=="Albania":
        url = "https://api.countrystatecity.in/v1/countries/al"
    elif my_country=="Andorra":
        url = "https://api.countrystatecity.in/v1/countries/ad"
    elif my_country=="Austria":
        url = "https://api.countrystatecity.in/v1/countries/at"
    elif my_country=="Belarus":
        url = "https://api.countrystatecity.in/v1/countries/by"
    elif my_country=="Belgium":
        url = "https://api.countrystatecity.in/v1/countries/be"
    elif my_country=="Bosnia and Herzegovina":
        url = "https://api.countrystatecity.in/v1/countries/ba"
    elif my_country=="Bulgaria":
        url = "https://api.countrystatecity.in/v1/countries/bg"
    elif my_country=="Croatia":
        url = "https://api.countrystatecity.in/v1/countries/hr"
    elif my_country=="Cyprus":
        url = "https://api.countrystatecity.in/v1/countries/cy"
    elif my_country=="Czech Republic":
        url = "https://api.countrystatecity.in/v1/countries/cz"
    elif my_country=="Denmark":
        url = "https://api.countrystatecity.in/v1/countries/dk"
    elif my_country=="Estonia":
        url = "https://api.countrystatecity.in/v1/countries/ee"
    elif my_country=="Finland":
        url = "https://api.countrystatecity.in/v1/countries/fi"
    elif my_country=="France":
        url = "https://api.countrystatecity.in/v1/countries/fr"
    elif my_country=="Germany":
        url = "https://api.countrystatecity.in/v1/countries/de"
    elif my_country=="Greece":
        url = "https://api.countrystatecity.in/v1/countries/gr"
    elif my_country=="Vatican City State (Holy See)":
        url = "https://api.countrystatecity.in/v1/countries/va"
    elif my_country=="Hungary":
        url = "https://api.countrystatecity.in/v1/countries/hu"
    elif my_country=="Iceland":
        url = "https://api.countrystatecity.in/v1/countries/is"
    elif my_country=="Ireland":
        url = "https://api.countrystatecity.in/v1/countries/ie"
    elif my_country=="Italy":
        url = "https://api.countrystatecity.in/v1/countries/it"
    elif my_country=="Latvia":
        url = "https://api.countrystatecity.in/v1/countries/lv"
    elif my_country=="Liechtenstein":
        url = "https://api.countrystatecity.in/v1/countries/li"
    elif my_country=="Lithuania":
        url = "https://api.countrystatecity.in/v1/countries/lt"
    elif my_country=="Luxembourg":
        url = "https://api.countrystatecity.in/v1/countries/lu"
    elif my_country=="Malta":
        url = "https://api.countrystatecity.in/v1/countries/mt"
    elif my_country=="Moldova":
        url = "https://api.countrystatecity.in/v1/countries/md"
    elif my_country=="Monaco":
        url = "https://api.countrystatecity.in/v1/countries/mc"
    elif my_country=="Montenegro":
        url = "https://api.countrystatecity.in/v1/countries/me"
    elif my_country=="Netherlands":
        url = "https://api.countrystatecity.in/v1/countries/nl"
    elif my_country=="North Macedonia":
        url = "https://api.countrystatecity.in/v1/countries/mk"
    elif my_country=="Norway":
        url = "https://api.countrystatecity.in/v1/countries/no"
    elif my_country=="Poland":
        url = "https://api.countrystatecity.in/v1/countries/pl"
    elif my_country=="Portugal":
        url = "https://api.countrystatecity.in/v1/countries/pt"
    elif my_country=="Romania":
        url = "https://api.countrystatecity.in/v1/countries/ro"
    elif my_country=="San Marino":
        url = "https://api.countrystatecity.in/v1/countries/sm"
    elif my_country=="Serbia":
        url = "https://api.countrystatecity.in/v1/countries/rs"
    elif my_country=="Slovakia":
        url = "https://api.countrystatecity.in/v1/countries/sk"
    elif my_country=="Slovenia":
        url = "https://api.countrystatecity.in/v1/countries/si"
    elif my_country=="Spain":
        url = "https://api.countrystatecity.in/v1/countries/es"
    elif my_country=="Sweden":
        url = "https://api.countrystatecity.in/v1/countries/se"
    elif my_country=="Switzerland":
        url = "https://api.countrystatecity.in/v1/countries/ch"
    elif my_country=="Turkey":
        url = "https://api.countrystatecity.in/v1/countries/tr"
    elif my_country=="Ukraine":
        url = "https://api.countrystatecity.in/v1/countries/ua"
    elif my_country=="United Kingdom":
        url = "https://api.countrystatecity.in/v1/countries/gb"

    r_final = requests.get(url, headers=headers)
    r_final_json = r_final.json()
    with open ("file_final.json", "w") as my_file:
        json.dump(r_final_json,my_file)

    with open("file_final.json", "r") as my_file:
        data_list = json.load(my_file)
        iso2_value=data_list.get("iso2")
        emoji_value=data_list.get("emoji")
        subregion_value=data_list.get("subregion")
        currency_name_value=data_list.get("currency_name")
        return (f"Short name (ISO2 country code): {iso2_value} \nNational flag: {emoji_value}\nSubregion: {subregion_value}\nCurrency: {currency_name_value}")

