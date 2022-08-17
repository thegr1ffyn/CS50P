import requests
import sys
import json

if len(sys.argv) ==2:
	try:
		value= float(sys.argv[1])
	except:
		sys.exit("Command Line argument is not a number")
else:
	print("Missing command-line argument")
	sys.exit(1)

try:
	r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
	response=r.json()
	bitcoin= response['bpi']['USD']['rate_float']
	totalamount= bitcoin*value
	print(f"${totalamount:,.4f}")
except requests.requestrException:
	print("RequestException")
	sys.exit(1)
