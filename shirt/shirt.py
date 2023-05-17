from PIL import Image, ImageOps
import sys

def main():
    small_argv()
    long_argv()
    shirt = sys.argv[1]
    after = sys.argv[2]
    argv_2_test()
    image_replace(shirt, after)


def small_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments ")
def long_argv():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
def argv_2_test():
    if not sys.argv[2].endswith(".jpg" or ".jpeg" or "png"):
        sys.exit("Invalid output")
    if not sys.argv[1].endswith(".jpg" or ".jpeg" or "png"):
        sys.exit("Invalid output")
    if sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")


def image_replace(shirt, after):
    try:
        shirt = Image.open(sys.argv[1])
    except FileNotFoundError:
        print("Input does not exist")
        return
    image1 = Image.open("shirt.png")
    shirt = ImageOps.fit(shirt, image1.size)
    shirt.paste(image1, mask = image1)
    shirt.save(after)
if __name__ == "__main__":
    main()