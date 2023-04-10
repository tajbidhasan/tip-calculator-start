#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total = input("What is the total bill?\n")
tip_percent = input("What is the percent tip would you like to add? 18 , 20, or 22?\n")

total_as_float = float(total)
trip_as_int = int(tip_percent)
tip_cal = total_as_float * (trip_as_int/100)

total_tip_bill = total_as_float + tip_cal

split = input("How many ways are you spliting the bill?\n")

split_as_int = int(split)

eachPays = total_tip_bill / split_as_int
eachPays = round(eachPays,2)
eachPays ="{:.2f}".format(eachPays)

print(f"Each person pays $ {eachPays}")