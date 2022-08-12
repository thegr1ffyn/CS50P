def main():
    platenum = input("Plate: ")
    if not platenum.isalnum() or (len(platenum) < 2 or len(platenum) > 6):
        print("Invalid")
        return False

    if is_valid(platenum):
        print("Valid")
    else:
        print("Invalid")


def is_valid(i):
    if   i.isalpha() or i[:2].isalpha() and i[-2:].isnumeric() and i[-2:][0] != "0":
        return True
    else:
        return False
main()