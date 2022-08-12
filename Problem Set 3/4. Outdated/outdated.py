months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if "," in date:
        month, day, year = date.replace(",", " ").split()
        try:
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        if day > 31 or month not in months:
            continue
        else:
            month = months.index(month) + 1
            break
    elif "/" in date:
        month, day, year = date.replace("/", " ").split()
        try:
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        if day > 31 or month > 12:
            continue
        break
    else:
        continue
    
print(f"{year}-{int(month):02}-{int(day):02}")