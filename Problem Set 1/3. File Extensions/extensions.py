# Both techniques for '.endswith' or 'in' can be used to solve the task

file=input("Enter filename: ")
new_file=file.lower()

if '.gif' in new_file:
    print("image/gif")

elif new_file.endswith('.jpg'):
    print("image/jpeg")

elif new_file.endswith('.jpeg'):
    print("image/jpeg")

elif new_file.endswith('.png'):
    print("image/png")

elif '.pdf' in new_file:
    print("application/pdf")

elif new_file.endswith('.txt'):
    print("text/plain")

elif new_file.endswith('.zip'):
    print("application/zip")

else:
    print("application/octet-stream")