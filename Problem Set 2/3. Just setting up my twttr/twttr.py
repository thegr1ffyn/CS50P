tweet=input("Write your Tweet: ")
new_tweet=""

vowels=["a","e","i","o","u"]

for i in range(len(tweet)):
    if tweet[i].lower() not in vowels:
        new_tweet+=tweet[i]

print(new_tweet)