months = [
    "abgdev",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    user_input = convert(input("Date: "))
    print(user_input)

# Check if input is in month-day-year format
# 1/1/1989
def convert(user_input):
    while True:
        if "/" in user_input:
            user_input = user_input.split("/")
            if user_input[0] not in months:
                year = int(user_input[2])
                month = int(user_input[0])
                day = int(user_input[1])
                if 1 <= day <= 31 and 1 <= month <= 12 and year > 999:
                    return f"{year}-{month:02}-{day:02}"
        # check if input is in
        if "," in user_input:
            user_input = user_input.replace(",", "")
            user_input = user_input.split(" ")
            if user_input[0] in months:
                month = user_input[0]
                month = months.index(month)
                month = int(month)
                year = int(user_input[2])
                day = int(user_input[1])
                if 1 <= day <= 31 and 1 <= month <= 12 and year > 999:
                    return f"{year}-{month:02}-{day:02}"

if __name__ == "__main__":
    main()
