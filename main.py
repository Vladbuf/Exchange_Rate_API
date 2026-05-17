import requests

class ExchangeRates():
    def __init__(self, currency, target_currency, amount):
        self.target_currency = target_currency
        self.currency = currency
        self.amount = amount
        self.result = self.get_result()
    def get_result(self):
        try:
            r = requests.get(f'https://open.er-api.com/v6/latest/{self.currency}', timeout=10)
            return r.json()
        except requests.HTTPError:
            print(f"Status code: {r.status_code}")
    def calculation(self):
        return self.result['rates'][self.target_currency] * self.amount
    def exchange(self):
        result = self.calculation()
        print(f"{self.amount} {self.currency} = {result:.2f} {self.target_currency}")


try:
    currency = input("Please type your currency (eg. RON, EUR): ").upper()
    amount = float(input("Please specify the amount: "))
    target_currency = input("Please type the currency you want exchanged: ").upper()
    exchange = ExchangeRates(currency, target_currency, amount)
    exchange.exchange()
except (requests.exceptions.Timeout, requests.ConnectionError):
    print("Request timed out. Please check if the internet works.")
except KeyError:
    print("\nPlease type a valid currency. Example: RON, USD, EUR, HUF...")
except ValueError:
    print("\nPlease input a valid number!")