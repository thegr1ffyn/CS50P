userinput=input("Greeting ").strip().lower()

if userinput.startswith("hello"):
    print("$0")
elif userinput.startswith("h"):
    print("$20")
else:
    print("$100")