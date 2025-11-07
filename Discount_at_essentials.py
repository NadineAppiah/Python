print("welcome to essentials")
range=5
while True:
    print("What is the cost of item in GHS")
    cost=float(input())
    if cost>=100:
        print("your discount is 15%")
        discount=15/100
        discount_amount=cost-(cost*discount)
        new_amount=cost-discount_amount
        print("Your new_amount is GHS", new_amount)
    
    if cost>=75 and cost<100:
        print("your discount is 10%")
        discount=10/100
        discount_amount=cost-(cost*discount)
        new_amount=cost-discount_amount
        print("Your new_amount is GHS", new_amount)
    
    if cost>=50 and cost<75:
        print("your discount is 5%")
        discount=5/100
        discount_amount=cost-(cost*discount)
        new_amount=cost-discount_amount
        print("Your new_amount is GHS", new_amount)
        
    if cost>50:
        print("your discount is 0%")
        dicount=0/100
        discount_amount=cost-(cost*dicount)
        new_amount=cost-discount_amount
        print("Your new_amount is GHS", new_amount)
        
    elif cost<=0:
        print("Invalid")
    
    
    