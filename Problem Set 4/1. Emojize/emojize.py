import emoji

user_input=input("Input: ")

output=emoji.emojize(user_input, language='alias')

print("Output", output)