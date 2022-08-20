def main():
    fraction= input("Fraction: ")
    frac_converted = convert(fraction)
    output = gauge(frac_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator,denominator = fraction.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            f= new_numerator/new_denominator

            if f<=1:
                p = int(f*100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except(ValueError,ZeroDivisionError):
            raise

def gauge(p):
    if p <= 1:
        print("E")

    elif p >= 99:
        print("F")

    else:
        print(f"{p}%")

if __name__ == "__main__":
    main()