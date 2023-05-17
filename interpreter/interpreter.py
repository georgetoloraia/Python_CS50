def main():
    user = calculator(input("Expression: ").strip())
    print(user)

def calculator(c):
    if "+" in c:
        c = c.split("+")
        c = float(c[0]) + float(c[1])
        return float(c)
    if "-" in c:
        c = c.split("-")
        c = float(c[0]) - float(c[1])
        return float(c)
    if "*" in c:
        c = c.split("*")
        c = float(c[0]) * float(c[1])
        return float(c)
    if "/" in c:
        c = c.split("/")
        c = float(c[0]) / float(c[1])
        return float(c)
    else:
        return "Invalid input! Please enter a valid expression."

main()
