import requests
import json

# coin = "bitcoin"
# date= "01-05-2022"
# dec = ["01-12-2022","01-12-2022","01-12-2022","01-12-2022","01-12-2022","01-12-2022","01-12-2022","01-12-2022"]
# feb = '24 February 2022'

# url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}&localization=false"
# print(url)
# x = requests.get(url)
# data = json.loads(x.text)
# print( data )
#print( data['market_data']['current_price']['usd'] )
coin = 'bitcoin'
vs_currency = 'usd'
time_start = 1638288000# dec 1 2021
time_end = 1648053000#march 24 2022


url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart/range?vs_currency={vs_currency}&from={time_start}&to={time_end}'


x = requests.get(url)
data = json.loads(x.text)
print(data.keys())
# for x in data['prices']:
#   print(x)





