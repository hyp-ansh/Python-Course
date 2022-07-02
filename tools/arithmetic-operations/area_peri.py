import sys

first01 = """Welcome to <<AREA AND PERI>>\nv1.0
Press ENTER to continue"""
print(first01)
input()
first02 = """Which shape
1. Square
2. Rectangle
3. Circle
4. Equilateral Triangle
5. RHS Triangle"""


def redo():
    print("\nYou want to continue?? (y/N)")
    re = str(input())
    if re == "y":
        option()
    elif re == "N":
        sys.exit("Thanks, For testing me out!!")
    else:
        print("Come On!!...say any one")
        redo()


def square():
    print("What is the length of the side :")
    side = float(input())
    side = round(side, 2)
    areas = round(side ** 2, 2)
    areas = str(areas)
    peris = round(side * 4, 2)
    peris = str(peris)
    print("Perimeter : " + peris + "\nArea : " + areas)
    redo()


def rectangle():
    print("What is the length : ")
    length = float(input())
    print("What is the breadth : ")
    breadth = float(input())
    arear = round(length * breadth)
    arear = str(arear)
    perir = round(2 * (length + breadth))
    perir = str(perir)
    print("Perimeter : " + perir + "\nArea : " + arear)
    redo()


def circle():
    print("What is the radius : ")
    r = float(input())
    arear = round(22 / 7 * r ** 2, 2)
    arear = str(arear)
    perir = round(2 * 22 / 7 * r, 2)
    perir = str(perir)
    print("Perimeter : " + perir + "\nArea : " + arear)
    redo()


def etri():
    print("What is the side : ")
    side = float(input())
    periet = round(3 * side, 2)
    periet = str(periet)
    areaet = round(1 / 4 * 3 ** (1 / 2) * side ** 2, 2)
    areaet = str(areaet)
    print("Perimeter : " + periet + "\nArea : " + areaet)
    redo()


def rt():
    print("What is the height : ")
    height = float(input())
    print("What is the base : ")
    base = float(input())
    hypo = ((height ** 2) + (base ** 2)) ** (1 / 2)
    areart = round(height * base, 2)
    areart = str(areart)
    perirt = round(height + base + hypo)
    perirt = str(perirt)
    print("Perimeter : " + perirt + "\nArea : " + areart)
    redo()


def reoption():
    shape = input()
    if shape == "1":
        square()
    elif shape == "2":
        rectangle()
    elif shape == "3":
        circle()
    elif shape == "4":
        etri()
    elif shape == "5":
        rt()
    else:
        print("Write the corresponding number!!")
    reoption()


def option():
    print(first02)
    reoption()


option()
