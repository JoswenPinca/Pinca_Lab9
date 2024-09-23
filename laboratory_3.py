monthly_salary = float(input("What is your monthly salary? "))
loan = float(input("How much will be your loan? "))

if monthly_salary >= 30000.00:
    max_amount = monthly_salary * 10
    if loan <= max_amount:
        print("You are eligible to loan!")
        months = int(input("How many months would you want to pay the loan? "))
        interest = loan * 0.10
        total_amount = interest + loan
        print(f"Loan Amount: ₱{loan:.2f}")
        print(f"Amount to pay back: ₱{total_amount:.2f}")
        print(f"Monthly payment over {months} months: ₱{total_amount / months:.2f}")
    else:
        print(f"Your loan amount is too high for your salary! Please enter loan below ₱{max_amount:.2f}")
else:
    print("You are not eligible for a loan because your salary is too low!")