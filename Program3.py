total_bill=3000
coupen_code=int(input("Enter Code: "))
premium_member=True
SAVE10=int(total_bill-((total_bill/100)*10))#"SAVE10": 10% discount on cart total
SUPER50=int(total_bill-((total_bill/100)*50))#"SUPER50": Flat 50 rupees discount
delivery=100

if coupen_code==2213 and (total_bill>1000 or premium_member==True): #Free shipping if customer is a premium member OR if bill after discount is 1000 rupees or more.
   print("The total bill with SAVE10 deal and free delivery is :" ,SAVE10)
elif coupen_code==3313 and (total_bill>1000 or premium_member==True): #Free shipping if customer is a premium member OR if bill after discount is 1000 rupees or more.
   print("The total bill with SUPER50 deal is and free delivery is :" ,SUPER50)
elif coupen_code==3313:
   print("The total bill with SUPER50 deal is :" ,SUPER50+delivery) #shipping costs 100 rupees.
elif coupen_code==2213:
   print("The total bill with SAVE10 deal is :" ,SAVE10+delivery) #shipping costs 100 rupees.
else:
   print("Invalid coupon code and total bill is: ",total_bill) #"Invalid coupon code"

