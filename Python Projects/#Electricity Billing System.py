# Electricity Billing System

def calculate_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (units - 500) * 6.00
    return bill


n = int(input("Enter number of customers: "))
grand_total = 0

for i in range(1, n + 1):
    print(f"\nCustomer {i}")
    cust_id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    ctype = input("Connection type (Home / Shop): ")
    units = float(input("Enter units consumed: "))

    bill = calculate_bill(units)
    meter_charge = 50
    tax = bill * 0.05
    final_bill = bill + meter_charge + tax
    grand_total += final_bill

    print("Customer ID   :", cust_id)
    print("Customer Name :", name)
    print("Connection    :", ctype)
    print("Units         :", units)
    print("Bill Amount   : Rs.", round(bill, 2))
    print("Meter Charge  : Rs.", meter_charge)
    print("Tax (5%)      : Rs.", round(tax, 2))
    print("Total Bill    : Rs.", round(final_bill, 2))

print("\nTotal Collection : Rs.", round(grand_total, 2))