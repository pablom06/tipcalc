# Python here
print("Welcome To Pablo's Pay Da Bill Calculator")
#Prompt the user to enter the amount on the bill
bill = float(input("How Much is the total bill?: "))
#Prompt the user for the % tip they'd like to leave
tip_input = int(input("What Percentage tip would you like to give?: %  "))
#Interactive if tip is less than 10% prompt response, if 0 prompt response, if 10%-20% prompt response,
#if greater than 20% prompt response
if tip_input >= 10 < 20:
    print("You are a great tipper!")
else:
    if tip_input >= 20:
        print("You are the world's greatest tipper!")
    else:
        if tip_input>0<10:
            print("You are so damn cheap!")
        else:
            if tip_input<=0:
                print("You should be ashamed of yourself. I never met anyone so cheap. I am going to call your mamma!")
                
#Prompt the user for the # of people splitting the bill
num_people = int(input("How many people are splitting the bill?:"))
print("\n")
#Calculate the sales tax
tax = (bill*.1)
total_bill=bill+tax
total_bill_tip=bill+tax+((tip_input*bill)/100)
 #(((float(((tip_input)) / 100+1) * total_bill / num_people)),2)
#Print the $ amount of the tip
tip_calc = ("%.2f" % float((tip_input) / 100 * bill))
print(f"Tip amount: ${tip_calc}")
#Calculate the value each person owes based on the bill and tips the user entered
payment_per_person = (total_bill_tip/num_people)
#convert total bill and tip amount to floats so they can be added
total_bill_float = float(bill)
tip_amount_float = float(tip_calc)
tip_and_total = (total_bill_float+tip_amount_float)
print(f"Total bill including tip: ${tip_and_total}")
print(f"Tax amount': ${tax}")
#Print what each person needs to pay
print(f"Total with tax and Tip: $ {total_bill_tip}")
print(f"Each person owes: ${payment_per_person}")




