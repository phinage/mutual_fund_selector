import requests

# Define the list of mutual fund tickers you want to retrieve portfolio information for
fund_tickers = ['VTIAX', 'VTSAX', 'VGSLX']
print(fund_tickers)

# Define the Yahoo Finance API endpoint
url = 'https://query1.finance.yahoo.com/v1/finance/quoteType/'

# Define the query parameters for the API request
params = {
    'symbols': ','.join(fund_tickers),
    'fields': 'symbol,longName,portfolioHoldings'
}

# Send a GET request to the Yahoo Finance API and retrieve the response
response = requests.get(url, params=params)

# Convert the response to JSON format
response_json = response.json()

# Loop through the list of mutual fund tickers and print the portfolio information for each fund
for fund in response_json['quoteResponse']['result']:
    print(f"Portfolio information for {fund['longName']} ({fund['symbol']}):")
    for holding in fund['portfolioHoldings']['holdings']:
        print(holding['holdingSymbol'], holding['holdingName'], holding['holdingValue']['fmt'])
    print('\n')
