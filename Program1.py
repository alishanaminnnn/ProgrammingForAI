units = 230 #units consumed
bill=0 # electricity bill

if units <= 100: #if units are below or equal to 100
    bill=units*5 #5 rupees per unit
elif   units>100 and units<=200: #if units are above 100 and equal and less than 200
    bill=units*8 #8 rupees per unit
elif   units>200: #if units are above or equal to 200
    bill=units*12

if bill>2000: # if the electricity bill above 2000
    bill=int(bill+((bill/100)*15)) # add 15% tax
    print("The total bill with 15% tax is ",bill)
else:
    print("The total bill is ",bill)
