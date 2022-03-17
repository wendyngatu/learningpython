price=1000000
good_credit=True

if good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"down_payment: ${down_payment}") 