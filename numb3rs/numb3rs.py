import re

def main():
    ip = input("IPv4 Address: ")
    output = validate(ip)
    print(output)

def validate(ip):
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        numbers = ip.split(".")
        if len(numbers) != 4:
            return False
        for i in range(int(numbers[0])):
            if i > 255:
                return False
        for num in numbers:
            if not (0 <= int(num) <= 255):
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()