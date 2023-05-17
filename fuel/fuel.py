
def main():
    user_input = calculate(input("Fraction: "))
    while True:
        if user_input is not None:
            print(user_input)
            break
        else:
            print("input valid")



def calculate(procent):

    while True:
        try:
            x, y = procent.split("/")
            x = int(x)
            y = int(y)
            if x > y or y == 0:
                raise ValueError
            procent = x / y * 100
            if procent <= 1:
                return "E"
            if procent >= 99:
                return "F"
            else:
                return (str(round(procent)) + '%')
        except (ValueError, ZeroDivisionError):
            return None

main()