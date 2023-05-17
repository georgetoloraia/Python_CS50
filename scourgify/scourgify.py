import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as input_file, open(sys.argv[2], "w") as output_file:
        d_reader = csv.DictReader(input_file, delimiter=",")
        # fieldnames = ["first_name", "last_name", "house"]
        d_writer = csv.DictWriter(output_file, ["first", "last", "house"])
        d_writer.writeheader()
        for row in d_reader:
            first, last = row["name"].split(",")
            d_writer.writerow({
                "first": last.strip(),
                "last": first.strip(),
                "house": row["house"]
                })

except FileNotFoundError:
    sys.exit("Could not read file")