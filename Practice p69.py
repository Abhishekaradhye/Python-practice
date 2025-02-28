'''A city wants to implement a smart billing system for residential electricity usage.

Each household gets a monthly balance of 5000 Rs for electricity usage.
The charges are:
2 Rs per unit for the first 100 units
5 Rs per unit for the next 200 units
10 Rs per unit for every unit above 300
If a household consumes more than 300 units, they get a 10% penalty on the total bill.
If a household consumes less than 150 units, they receive a 5% cashback on their bill.
Task:
Write a program to calculate the final electricity bill for a household based on their monthly usage and check if they have remaining balance or need to pay extra.'''

def smart_electricity_billing(monthly_balance, units):
    bill = 0

    # Calculate base bill based on unit slabs
    if units <= 100:
        bill = units * 2

    elif 101 <= units <= 300:
        bill = (100 * 2) + ((units - 100) * 5)

    else:  # units > 300
        bill = (100 * 2) + (200 * 5) + ((units - 300) * 10)
        bill = bill + (bill * 0.1)  
        
    if units < 150:
        cashback = bill * 0.05
        bill -= cashback  
        monthly_balance += cashback  
        
    if monthly_balance >= bill:
        print("\nThank you! Your bill is successfully paid.")
        remaining_balance = monthly_balance - bill
        print(f"Remaining balance: Rs. {remaining_balance}")
    else:
        print(f"\nInsufficient funds! You are short of Rs. {bill - monthly_balance}. Please recharge.")

    return bill



print("Dear customer, your smart electricity bill is Rs.", smart_electricity_billing(5000, 200))
print("Dear customer, your smart electricity bill is Rs.", smart_electricity_billing(5000, 350))
print("Dear customer, your smart electricity bill is Rs.", smart_electricity_billing(5000, 800))



# Response :

# Thank you! Your bill is successfully paid.
# Remaining balance: Rs. 4300
# Dear customer, your smart electricity bill is Rs. 700

# Thank you! Your bill is successfully paid.
# Remaining balance: Rs. 3130.0
# Dear customer, your smart electricity bill is Rs. 1870.0

# Insufficient funds! You are short of Rs. 1820.0. Please recharge.
# Dear customer, your smart electricity bill is Rs. 6820.0
