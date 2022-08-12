def main():
    time = input("Enter time: ")
    converted_time = convert(time)
    if converted_time>=7 and converted_time<=8:
        print("breakfast time")

    elif converted_time>=12 and converted_time<=13:
        print("lunch time")

    elif converted_time>=18 and converted_time<=19:
        print("dinner time")


def convert(time):
    hours, minutes= time.split(":")

    hours=float(hours)+(float(minutes)/60)
    return hours

if __name__ == "__main__":
    main()