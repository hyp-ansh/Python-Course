days = int(input("Enter Day : "))
years = (days // 365)
months = (days - (years * 365)) // 30
remain_days = ((days - (years * 365)) - (months * 30))
print(f"{days} Days is {years} years, {months} month, {remain_days} days")
