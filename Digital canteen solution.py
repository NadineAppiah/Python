"""
Problem Statement- The canteen staff find it difficult to manage students purchases during lunch-time, create a simple Python-based digital canteen assistant that runs on a laptop to calculate totals, manage change, and track sales.

Reframed Problem - Create a Python Program that helps the canteen staff to easily process students purchase easily by taking their orders, calculating their total with tax, handling payment and giving their change.

What I Know-
Basic Python Programming
Variables
Conditional Statements
Taking Input
Basic Calculations(Addition,Subtraction,Multiplication&Division)
Integer Division
Loops
Calculating Change(amount paid-total price)
Calculating Subtotals(price * quantity)

What I Need to Know-
Calculating and Applying tax
Calculating the total with tax

Research-
I learned how to:
calculate tax; Tax amount = subtotal*(tax percentage)
calculate the total with tax; Total = subtotal+tax amount
"""
sales=[]
menu= {
 "Mandazi": 10.00,
 "Plain rice": 8.50,
 "Jollof rice": 13.00,
 "Fried rice": 15.00,
 "Chapati": 12.80,
 "Juice": 20.00,
 "Soda": 11.30,
 "Chicken": 9.00,
 "Fish": 7.60,
 "Fried egg": 4.00,
 "Boiled egg": 3.50,
}

tax_rate=0.08  #8%
order=0

print('Welcome!, What would you like to do')
print("Program menu")
print(" 1. Receive an order\n 2. Display all sales")

command=input("Enter option 1 or 2 ")

if command == '1':
    print("Menu:", menu)
    
elif command == '2':
    print("Displaying all sales...")
    if not sales:
        print("No sales recorded")
    else:
        print("Total sales:\n Order details:")
        total_sales= sum(sale["total"] for sale in sales)    
        print(f"Total Sales: GHS {total_sales:.2f}") 
else:
    print("N/A")

while True:
    order=input("What would you like to buy?( type 'done' to end):)")
    if order == 'done':
        break
    elif order != menu:
        print("Invalid order, please choose from the menu")
    else:
        print("quantity")
        quantity=int(input("How many?"))
        order = order + quantity

else:
    print("Total amount")
    total_amount=input("Total of things ordered")
    sub_total=price*quantity
    tax_amount=sub_total*tax_rate
    total_amount=tax_amount+total_amount
    
amount_paid=float(input("Enter amount being paid"))



