loan_amount = float(input("Enter loan amount: $"))
annual_rate = float(input("Enter annual interest rate (%): "))
monthly_payment = float(input("Enter monthly payment: $"))

monthly_rate = (annual_rate / 100) / 12

first_month_interest = loan_amount * monthly_rate
if monthly_payment <= first_month_interest:
    print("Your monthly payment is too small. It doesn't even cover the interest,")
    print("so the loan would never be paid off. Try a larger payment.")
else:
    balance = loan_amount
    months = 0
    total_interest = 0

    while balance > 0:
        interest = balance * monthly_rate
        total_interest += interest
        balance = balance + interest

        if monthly_payment >= balance:
            balance = 0
        else:
            balance = balance - monthly_payment

        months += 1

    print("\n--- Loan Summary ---")
    print(f"Months to pay off: {months}")
    print(f"Total interest paid: ${total_interest:,.2f}")