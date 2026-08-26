print("Choose the conversion you want to perform:")
print("1. kg to lb")
print("2. lb to kg")
choice = int(input("Enter your choice (1 or 2): "))
unit = int(input("Insert data:"))
if(choice==1):
 ansr = unit*2.20462
 print( f" {ansr} lb")

elif (choice==2):
 ansr = unit*0.453592
 print( f" {ansr} kg")

else:
 print("Invalid input.")