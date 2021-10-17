Choice = input("Enter a choice 1.Pounds to Kilograms 2. Kilograms to Pounds")
if int(Choice) == 1 :
   Weight_In_Pounds = input("Enter your weight in pounds")
   Weight_In_Kilograms = float(Weight_In_Pounds) / 2.20462262
   print(f"Your Weight in kilograms is {Weight_In_Kilograms}")
elif  int(Choice) == 2 :
    Weight_In_Kilograms = input("Enter weight in kilograms")
    Weight_In_Pounds = float(Weight_In_Kilograms) * 2.20462262
    print(f" Your weight in pounds is {Weight_In_Pounds}")
else:
    print("You have entered an invalid option. Please try again")
