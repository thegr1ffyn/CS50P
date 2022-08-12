while True:
    fuel=input("Enter fraction: ")
    try:
        numerator,denominator=fuel.split("/")

        new_numerator = int(numerator)
        new_denominator = int(denominator)

        div= new_numerator/new_denominator

        if div <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

percent = round ( div * 100 )

if percent <= 1:
    print("E")

elif percent >= 99:
    print("F")

else:
    print(f"{percent}%")
