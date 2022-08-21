import random

def main():
    lvl = get_level()
    num_correct = generate_integer(lvl)
    print('Score:', num_correct)

def get_level():
    while True:
        try:
            i = int(input('Select Level: '))
            if i not in range(1,4):
                raise ValueError
            else:
                return i
        except ValueError:
            continue

def generate_integer(level):
    score = 0
    if level == 1:
        for _ in range(10):
            a = random.randint(0,9)
            b = random.randint(0,9)
            attempt = 0
            while True:
                if attempt == 3:
                    print((f'{a} + {b} = {a+b}'))
                    break
                i = int(input(f'{a} + {b} = '))
                if i == a + b:
                    score += 1
                    break
                else:
                    print('EEE')
                    attempt += 1
        return score
    elif level == 2:
        for _ in range(10):
            a = random.randint(10,99)
            b = random.randint(10,99)
            attempt = 0
            while True:
                if attempt == 3:
                    print((f'{a} + {b} = {a+b}'))
                    break
                i = int(input(f'{a} + {b} = '))
                if i == a + b:
                    score += 1
                    break
                else:
                    print('EEE')
                    attempt += 1
        return score
    else:
        for _ in range(10):
            a = random.randint(100, 999)
            b = random.randint(100, 999)
            attempt = 0
            while True:
                if attempt == 3:
                    print((f'{a} + {b} = {a+b}'))
                    break
                i = int(input(f'{a} + {b} = '))
                if i == a + b:
                    score += 1
                    break
                else:
                    print('EEE')
                    attempt += 1
    return score

if __name__ == "__main__":
    main()
