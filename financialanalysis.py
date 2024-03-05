import requests
import matplotlib.pyplot as plt

# Define your FMP API key
api_key = '194b4b2704bf876cb92927b427b518d1'

# Define the endpoint for fetching income statement
# endpoint = 'https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL'


company = "AAPL"
years = 10

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")
income_statement = income_statement.json()

revenues = list(reversed([income_statement[i]['revenue'] for i in range (len(income_statement))]))
profits = list(reversed([income_statement[i]['grossProfit'] for i in range (len(income_statement))]))


plt.plot(revenues, label="Revenue")
plt.plot(profits, label="Profit")
plt.title("AAPL Revenue and Profit")
plt.legend(loc="upper left")
plt.show()
#adding this comment for testing
