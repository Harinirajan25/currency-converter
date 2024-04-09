from forex_python.converter import CurrencyRates
print("                Real Time Currency Converter                   ")
print("---------------------------------------------------------------")
def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == "__main__":
    while True:
       
        amount = float(input("Enter the amount to convert (or type '0' to exit): "))
        if amount == 0:
                print("                   Exiting the currency converter. Goodbye!")
                break
        elif amount>=0:
            from_currency = input("Enter the source currency code (e.g., USD): ").upper()
            to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

            converted_amount = convert_currency(amount, from_currency, to_currency)
            
            print(" \n          -----------------------------------------" )   
            print(f"           {amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}.            ")
            print("           ---------------------------------------- ")
        else:
            print("Invalid input. Please enter valid numeric values.")
