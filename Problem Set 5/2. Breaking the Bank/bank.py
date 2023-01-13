def main():
    greeting = input ("Greeting: ")
    value_print= value(greeting)
    print(f"${value_print}")

def value(greeting):
    greeting = greeting.lower().strip()

    if greeting.startswith('hello'):
        return 0
    elif greeting[0].startswith('h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()