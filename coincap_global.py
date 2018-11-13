import json
import requests
from datetime import datetime

currency = 'JPY'

global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' + currency

request = requests.get(global_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

active_currencies = results['data']['active_cryptocurrencies']
#print(active_currencies)
active_markets = results['data']['active_markets']
bitcoin_percentage = results['data']['bitcoin_percentage_of_market_cap']
last_updated = results['data']['last_updated']
global_cap = int(results['data']['quotes'][currency]['total_market_cap'])
global_volume = int(results['data']['quotes'][currency]['total_volume_24h'])

active_currencies_string ='{:,}'.format(active_currencies)
active_markets_string ='{:,}'.format(active_markets)
global_cap_string ='{:,}'.format(global_cap)
global_volume_string ='{:,}'.format(global_volume)

last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d %Y at %I:%M%p')

print()
print('There are currently '+ active_currencies_string + ' active active_cryptocurrencies and ' + active_markets_string + ' active markets.')
print('The global cap of all cryptos is '+ global_cap_string + ' and the 24th global volume is '+ str(global_volume)+ '.')
print('Bitcoin\'s total percentage of the global cap is '+ str(bitcoin_percentage) + '%. ')
print()
print("This information was last updated on "+ last_updated_string+ '.')
