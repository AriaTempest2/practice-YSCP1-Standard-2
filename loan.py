def display():
    print("##############################################")
    print("### Welcome to the Loan Payment Calculator ###")
    print("##############################################\n\n")

    total = float(input("Enter the loan principal amount ($): "))
    interest = float(input("Enter the annual interest rate (in %, e.g., 5 for 5%): "))
    loan = float(input("Enter the loan term in years: "))  

    print("\nLOAN PAYMENT SUMMARY -")
    print(f"Loan Principal: ${total:.2f}")
    print(f"Annual Interest Rate: {interest:.2f}%")
    print(f"Loan Term: {loan} years")

    interest_rate = interest / 100 / 12
    months = loan * 12

    if interest_rate > 0:
        monthly_payment = (total * interest_rate) / (1 - (1 + interest_rate) ** -months)
    else:
        monthly_payment = total / months

    total_payment = monthly_payment * months

    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment Over Loan Term: ${total_payment:.2f}")

display()

