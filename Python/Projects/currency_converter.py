# ask user to provide input
# first user inputs are from currency to currency 
# secondly user amount
# this program supports to only USD to INR

from_currency = input("From currency:")
to_currency = input("to currency:")
amount = input("enter amount in dollars:")

def currency_converter():
    if from_currency == "USD" and to_currency == "INR":
        result = float(amount) * 83.38
        print("converted amount USD to INR:" + str(result) + "")
    else:
        print("entered invalid currency type")
        
currency_converter()
                
         
        
        
    