def main():
    user = convert(input("File name: ").lower().strip())
    print(user)

def convert(file):
    if file.endswith(".jpeg") or file.endswith(".jpg"):
        file = "image/jpeg"
        return file
    elif file.endswith(".gif"):
        file = "image/gif"
        return file
    elif file.endswith(".png"):
        file = "image/png"
        return file
    elif file.endswith(".pdf"):
        file = "application/pdf"
        return file
    elif file.endswith(".txt"):
        file = "text/plain"
        return file
    elif file.endswith(".zip"):
        file = "application/zip"
        return file
    else:
        file = "application/octet-stream"
        return file

main()