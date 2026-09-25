num_customers = int(input("Enter total number of customers: "))

total_bill_amount = 0.0
highest_bill = -1.0
highest_bill_customer = None


SURCHARGE_THRESHOLD = 1500.0  
SURCHARGE_RATE = 0.05         


for i in range(1, num_customers + 1):
    print(f"\n--- Processing Customer {i} ---")
    
    units = float(input(f"Enter units consumed for Customer {i}: "))
    while units < 0:
        print("Invalid input! Units cannot be negative.")
        units = float(input(f"Please re-enter valid units for Customer {i}: "))

    
    if units <= 100:
        base_bill = units * 3.0
    elif units <= 200:
        base_bill = (100 * 3.0) + ((units - 100) * 4.5)
    else:
        base_bill = (100 * 3.0) + (100 * 4.5) + ((units - 200) * 6.0)

   
    if base_bill > SURCHARGE_THRESHOLD:
        surcharge = base_bill * SURCHARGE_RATE
    else:
        surcharge = 0.0

    final_bill = base_bill + surcharge

   
    if units <= 100:
        category = "Low Consumer"
    elif units <= 200:
        category = "Moderate Consumer"
    else:
        category = "High Consumer"

    
    print(f"Base Bill: Rs. {base_bill:.2f}")
    if surcharge > 0:
        print(f"Surcharge (5%): Rs. {surcharge:.2f}")
    print(f"Final Payable Bill: Rs. {final_bill:.2f}")
    print(f"Category: {category}")

    
    total_bill_amount += final_bill
    if final_bill > highest_bill:
        highest_bill = final_bill
        highest_bill_customer = i


print("\n Billing Summary")
if num_customers > 0:
    average_bill = total_bill_amount / num_customers
    print(f"Customer with Highest Bill : Customer {highest_bill_customer} (Rs. {highest_bill:.2f})")
    print(f"Average Bill Across All Customers: Rs. {average_bill:.2f}")
else:
    print("No customer data to display.")