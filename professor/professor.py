import random


def main():
    level = get_level()
    score = 0
    kaoche = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        problem = f"{x} + {y} = "
        result = x + y
        attemps = 0

        while True:
            answer = input(problem)
            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
                attemps += 1
                if attemps >= 3:
                    print(f"the anser is: {result}")
                    break
                continue
            if answer != result:
                print("EEE")
                score += 1
                if score >= 3:
                    print(f"the anser is: {result}")
                    break
            if answer == result:
                kaoche += 1
                break
    print(f"Score: {kaoche}")



def get_level():
    while True:
        level = input("input level as 1, 2 or 3: ")
        level = str(level)
        if not level.isalpha():
            level = int(level)
            if 1 <= level <= 3:
                return level


def generate_integer(level):
        if level == 1:
            level = random.randrange(0, 10)
            return level
        elif level == 2:
            level = random.randrange(10, 100)
            return level
        elif level == 3:
            level = random.randrange(100, 1000)
            return level


if __name__ == "__main__":
    main()