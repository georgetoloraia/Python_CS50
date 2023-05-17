from datetime import date, timedelta
import inflect
import re
import sys

p = inflect.engine()

def main():
    birthday = input("Birth date: ")
    try:
        if valid_format(birthday):
            mins = minutes(birthday)
            print(minutes_to_words(mins))
        else:
            sys.exit("Invalid format")
    except:
        sys.exit("Something went wrong")

def minutes(birthday):
    year, month, day = birthday.split("-")
    formated_birthday = date( year = int(year), month = int(month), day = int(day))
    today = date.today()
    diff = today - formated_birthday
    minutes = int(diff.total_seconds() // 60)
    return minutes

def minutes_to_words(minutes):
    word = p.number_to_words(minutes, andword="")
    return f"{word.capitalize()} minutes"

def valid_format(birth_date):
    pattern = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}"
    if re.match(pattern, birth_date):
        return True
    return False

if __name__ == "__main__":
    main()