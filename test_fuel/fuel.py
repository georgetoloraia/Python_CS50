def main():
    user_input = input("Fraction: ")
    fraction = convert(user_input)
    percentage1 = gauge(fraction)
    print(percentage1)


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y or y == 0:
                raise ValueError

            procent = x / y * 100
            return procent
        except ValueError:
            return "ValueError"
        except ZeroDivisionError:
            return "ZeroDivisionError"


def gauge(percentage):
    if 0 < percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    if 2 <= percentage < 99:
        # percentage = percentage * 100
        # percentage = int(percentage)
        percentage = round(percentage)
        return f"{percentage}%"
        # return percentage


if __name__ == "__main__":
    main()