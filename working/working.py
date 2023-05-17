import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.match(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s)
    if not match:
        raise ValueError

    start_hour, start_minute, start_meridiem = int(match.group(1)), int(match.group(2) or 0), match.group(3)
    finish_hour, finish_minute, finish_meridiem = int(match.group(4)), int(match.group(5) or 0), match.group(6)

    if start_hour > 12 or start_minute >= 60 or finish_hour > 12 or finish_minute >= 60:
        raise ValueError

    if start_hour == 12 and start_meridiem == "AM":
        start_hour = 0
    elif start_hour != 12 and start_meridiem == "PM":
        start_hour += 12

    if finish_hour == 12 and finish_meridiem == "AM":
        finish_hour = 0
    elif finish_hour != 12 and finish_meridiem == "PM":
        finish_hour += 12

    return f"{start_hour:02d}:{start_minute:02d} to {finish_hour:02d}:{finish_minute:02d}"

if __name__ == "__main__":
    main()

