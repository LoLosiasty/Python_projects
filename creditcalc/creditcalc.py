import math
import argparse
# Entry parameters
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"])
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--principal")
args = parser.parse_args()
# Validation of parameters
if (args.type not in ["diff", "annuity"]) \
        or (args.type == "diff" and args.payment is True) \
        or bool(args.interest) is False\
        or (bool(args.interest) is True and float(args.interest) < 0)\
        or (bool(args.payment) is True and int(args.payment) < 0)\
        or (bool(args.periods) is True and int(args.periods) < 0)\
        or (bool(args.principal) is True and int(args.principal) < 0):
    print("Incorrect parameters")
    exit()

# calculations
if args.type == "diff":                                                 # payments per period
    periods = int(args.periods)
    principal = int(args.principal)
    interest = ((float(args.interest) / 12) / 100)
    i = 1
    full_payment = 0
    while i <= periods:
        daily_payment = math.ceil((principal / periods) + (interest * (principal - ((principal * (i - 1)) / periods))))
        full_payment += daily_payment
        print(f'Month {full_payment}: payment is {daily_payment}')
        i += 1
    overpayment = full_payment - principal
    print(f'Overpayment = {overpayment}')


if all(bool(arg) is True for arg in (args.principal, args.payment, args.interest)) and args.type == "annuity":
    principal = int(args.principal)                                     # time of repaying the loan
    payment = int(args.payment)
    interest = ((float(args.interest) / 12) / 100)
    months = math.ceil(math.log(payment / (payment - (interest * principal)), 1 + interest))
    overpayment = payment * months - principal
    print(f'It will take {int(months / 12)} years and {months % 12} months to repay this loan!')
    print(f'Overpayment = {overpayment}')


if all(bool(arg) is True for arg in (args.principal, args.periods, args.interest)) and args.type == "annuity":
    principal = int(args.principal)                                     # payment per period
    months = int(args.periods)
    interest = ((float(args.interest) / 12) / 100)
    payment = math.ceil(principal * (interest * ((1 + interest) ** months) / (((1 + interest) ** months) - 1)))
    overpayment = payment * months - principal
    print(f'Your monthly payment = {payment}!')
    print(f'Overpayment = {overpayment}')


if all(bool(arg) is True for arg in (args.payment, args.periods, args.interest)) and args.type == "annuity":
    annuity = int(args.payment)                                         # loan principal
    months = int(args.periods)
    interest = ((float(args.interest) / 12) / 100)
    principal = math.floor(annuity / ((interest * (1 + interest) ** months) / (((1 + interest) ** months) - 1)))
    overpayment = annuity * months - principal
    print(f'Your loan principle = {principal}!')
    print(f'Overpayment = {overpayment}')
