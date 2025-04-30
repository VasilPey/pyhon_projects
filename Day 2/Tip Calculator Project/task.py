print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_num=((bill / people)*(tip/100+1))
round(tip_num,3)
final_sum=bill + tip_num
round(final_sum,2)
print(f"The tip is: {tip}%,which is {tip_num} $")
print(f"The bill is: {bill} $")
print(f"The bill with the tip is: {final_sum} $")
bill_per_person=(final_sum/people)
print(f"Each person should pay: {bill_per_person} $")

