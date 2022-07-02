option = input("This is tempature conversion program.\n\
What you want to do\n\
(0) Celsius To Fahrenheit\n\
(1) Fahrenheit To Celsius\n")
def cf():
    celsius = float(input("Temperature in Celsius : "))
    fahrenheit = float(celsius * 9/5 + 32)
    print(f"Temperature in Fahrenheit is {fahrenheit}°")


def fc():
    fahrenheit = float(input("Temprature in Fahrenheit : "))
    celsius = float((fahrenheit - 32) * 5/9)
    print(f"Temparture in Celsius is {celsius}")


def choose():
    if option == "0":
        cf()
    elif option == "1":
        fc()
    else:
        print("Invalid Input")
        choose()

choose()