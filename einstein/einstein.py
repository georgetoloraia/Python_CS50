
def main():
    m = calculate(input("input the m: "))
    print(m)

def calculate(m):
    m = int(m)
    c = int(300000000)
    E = m * (c ** 2)
    return E

main()