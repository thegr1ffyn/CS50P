def main():
    s=input()
    print(convert(s))

def convert(s):
    s=s.replace(":)","🙂").replace(":(","🙁")
    return s

main()