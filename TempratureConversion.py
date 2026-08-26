print("Choose the conversion you want to perform:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))
unit = int(input("Insert data:"))
if(choice==1):
 ansr = unit*(9/5)
 ansr+=32
 print( f" {ansr} deg Farenheit")

elif (choice==2):
 ansr = (unit-32)*(5/9)
 print( f" {ansr} deg Celcius")

else:
 print("Invalid input.")
