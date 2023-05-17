def main():
    inputed_time = convert(input("What time is it?: "))
    if 7 <= inputed_time <= 8:
        print("breakfast time")
    elif 12 <= inputed_time <= 13:
        print("lunch time")
    elif 18 <= inputed_time <= 19:
        print("dinner time")
    else:
        None

def convert(time):
    hours, time = time.split(":")
    time = float(time) / 60
    hours = float(hours)
    hours_time = hours + time
    return hours_time

if __name__ == "__main__":
    main()