height = float(input("Insert your height in meter:"))
weight = float(input("Insert your weight in kg:"))
bmi = weight/(height**2)
print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Healthy weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("Obesity Class 1")
elif bmi >= 35 and bmi <= 39.9:
    print("Obesity Class 2")
else:
    print("Obesity Class 3")
