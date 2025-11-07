print("*****************************************")
print("* Welcome to Ashesi Payroll System!     *")
print("*****************************************")
print("* 1. Enter your monthly salary (GHS)    *")
print("* 2. Enter your years of service (>0yrs)*")
print("* 3. Enter '0' to exit this program.    *")
print("*****************************************")
bonus_amount = 0.0
while True:
    print("") #Leaves a line between each iteration
    print("Enter your monthly salary or '0' to exit: ")
    salary_earned = float(input())
    if salary_earned == float(0):
        print("8<----------------------------------\n")
        print("You have entered: '", int(salary_earned), "' to exit :(")
        print("Thanks for using our program!")
        print("\n8<----------------------------------")
        exit()#terminate program 
    print("Enter the number of years you have worked at this company: ")
    years_worked = int(input())

    if years_worked < 3 and years_worked > 0:
        print("No bonus")
    elif years_worked >= 3 and years_worked <= 5:
        bonus_amount = 0.1 * salary_earned
        salary_earned += bonus_amount
print ("Bonus is 10% of monthly salary: GHS", bonus_amount, ", so total amount is: GHS " + str(salary_earned))
    elif years_worked >= 6 and years_worked <= 10:
        bonus_amount = 0.15 * int(salary_earned)
        salary_earned = salary_earned + bonus_amount
        print ("Bonus is 15% of monthly salary: GHS", bonus_amount, ", so total amount is: GHS " + str(salary_earned))
    elif years_worked > 10:
        bonus_amount = 0.2 * salary_earned
        salary_earned = salary_earned + bonus_amount
        print ("Bonus is 20% of monthly salary: GHS", bonus_amount, ", so total amount is: GHS " + str(salary_earned))
    else:
        print("Number of years provided,", years_worked, " is out of the required scope of 0 years to more than 10 years!")
        print("Enter valid values!")
        continue #What will happen here?