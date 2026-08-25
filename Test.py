balance = float(input("Please enter your balance: $"))
print("Menu:")
print("1. Burger")
print("2.Pizza")
print("3. Pasta")
burger =5.60
pizza = 8.20
pasta = 7.50
tax = 0.07
option = int(input("Please select an option (1-3): "))
if option == 1 and balance >= burger:
    balance -= burger*(1 + tax)
    print(f"You have ordered a Burger. Your remaining balance is: ${balance:.2f} and the tax is: ${burger*tax:.2f}")
elif option == 2 and balance >= pizza:
    balance -= pizza*(1 + tax)
    print(f"You have ordered a Pizza. Your remaining balance is: ${balance:.2f} and the tax is: ${pizza*tax:.2f}")
elif option == 3 and balance >= pasta:
    balance -= pasta*(1 + tax)
    print(f"You have ordered Pasta. Your remaining balance is: ${balance:.2f} and the tax is: ${pasta*tax:.2f}")
else:
    print("Invalid option or insufficient funds.")
