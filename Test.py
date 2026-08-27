capital =0
rate=0
years=0

while True:
    capital=float(input("Insert capital: "))
    if capital<0:
        print("Capital can't be less than zero.")
    else:
        break
while True:
    rate=float(input("Insert rate: "))
    if rate<0:
        print("Interest rate can't be less than zero.")
    else:
        break
while True:
    years=float(input("Insert years: "))
    if years<0:
        print("Years can't be less than zero.")
    else:
        break
interest=(1+(rate/100))** years
interest*=capital
print(f"${interest:.2f}")
