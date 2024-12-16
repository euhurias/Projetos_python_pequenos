import pycountry

def get_currency(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        currency = pycountry.currencies.get(numeric=country.numeric)
        return f"The currency of {country_name} is {currency.name}"
    except:
        return "Country not found or currency information unavailable"


country_name = input("Enter country name: ")

print(get_currency(country_name))
