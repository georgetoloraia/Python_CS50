import sys

user = sys.argv

if len(user) == 1:
    sys.exit("Too few command-line arguments")

if len(user) > 2:
    sys.exit("Too many command-line arguments")

if not user[1].endswith(".py"):
    sys.exit("Not a Python file")

filename = user[1]
print(filename)
if len(user) == 2:
    try:
        if filename.endswith(".py"):
            with open(filename) as f:   # "/workspaces/128076435/lines/" +
                lines = f.readlines()
                # print(lines)
                code_lines = 0

                for line in lines:
                    line = line.strip()
                    if line.startswith("#"):
                        continue
                    if not line:
                        continue
                    code_lines += 1
                print(code_lines)
    except:  # FileNotFoundError
        sys.exit("Not a Python file")
