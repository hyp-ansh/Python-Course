r = float(input("Radius : "))
p = float(2 * 22/7 * r)
cir = round(p, 2)
if cir >= 0:
    print(f"Cir : {cir}")
elif cir < 0:
    print("error")
