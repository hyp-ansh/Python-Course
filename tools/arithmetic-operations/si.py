print("This program calculates Simple Intrest.")
principle = float(input("Enter Principle (in ₹): "))
rate = float(input("Enter Rate of interest : "))
time = float(input("Enter time (in years) : "))
si = (principle * rate * time) / 100
amount = principle + si
print(f"S. I. = ₹{si}\nTotal amount = ₹{amount}")
