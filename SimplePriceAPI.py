#BasicCryptoPrice
#This program should find the price of Bitcoin, Ethereum, and XRP
#Corey R
#API KEY: PUT YOUR OWN API KEY HERE


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def PP(unrounded, name):    #Function prints rounded price of chosen crypto
    price = round(unrounded,2)
    print(f'The current {name} price is: ${price:,}')

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'   #Endpoint
parameters = {
'start':'1',
'limit':'5000',
'convert':'USD'   #Chosen currency to convert to
}

headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': 'PUT API HERE',   #INSERT API KEY HERE
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text) 
    print('Success!')  #Outputs if everything works.
    
    Bitcoin=data['data'][0]['quote']['USD']['price']
    Ethereum=data['data'][1]['quote']['USD']['price']    #parses JSON data and grabs price from API
    XRP=data['data'][3]['quote']['USD']['price']
    
    PP(Bitcoin, 'Bitcoin')
    PP(Ethereum, 'Ethereum')
    PP(XRP, 'XRP')
    
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print('Error, connection failed')
    print(e)

