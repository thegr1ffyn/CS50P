def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_wo_sign=d.replace("$"," ")
    return float(d_wo_sign)


def percent_to_float(p):
    p_wo_percent=p.replace("%"," ")
    p_conv=float(p_wo_percent)/100
    return p_conv


main()