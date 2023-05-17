import requests
import sys
import json

def main():
    while True:
        try:
            if sys.argv == "":
                print("Missing command-line argument")
            from_api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            float_dollar = from_api.json()

            float_rate = float(float_dollar["bpi"]["USD"]["rate_float"])
            argument = sys.argv[1]
            float_rate = float_rate * float(argument)
            print(argument)
            print(f"${float_rate:,.4f}")
            sys.exit()

        except requests.RequestException:
            continue

if __name__ == "__main__":
    main()
