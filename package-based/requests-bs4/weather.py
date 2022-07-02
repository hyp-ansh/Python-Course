import requests as r

def celsius(c):
    temp = str((c - 273.15)).split(".")
    return f"Temprature in Asansol is {temp[0]}° C"


result = r.get(
    "https://api.openweathermap.org/data/2.5/forecast?id=1278314&appid=eecf3d4f578ee89fa4a0d087469c8b91")
#curtemp = result["main"]["temp"]

#print(celsius(curtemp))
print(result)
