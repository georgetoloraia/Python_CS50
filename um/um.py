import re

def main():
    print(count(input("Text: ")))

def count(s):
    i = 0
    while True:
        if  re.search(r"(um)", s, re.IGNORECASE):
            if  re.search(r"\w+(um)", s, re.IGNORECASE):
                s = re.sub(r"\w+(um)", "", s, 1, re.IGNORECASE)
            elif  re.search(r"(um)\w+", s, re.IGNORECASE):
                s = re.sub(r"(um)\w+", "", s, 1, re.IGNORECASE)
            else:
                s = re.sub(r"um", "", s, 1, re.IGNORECASE)
                i+=1
        else:
            return i



if __name__=="__main__":
    main()