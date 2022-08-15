import inflect

p=inflect.engine()

names = [ ]
text = "Adieu, adieu, to "

while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

join_names = p.join(names)
print(text + join_names)