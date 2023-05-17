import re

def main():
    out = parse(input("HTML: "))
    print(out)

def parse(s):
    pattern = r'[^\w]src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"'
    match = re.search(pattern, s)
    if match:
        url = match.group(1)
        if not "https" in url:
            url = re.sub(r'youtube\.com/embed/', 'youtu.be/', url)
            url = url.replace("http", "https")
            return url
        url = re.sub(r'youtube\.com/embed/', 'youtu.be/', url)
        url = url.replace("www.", "")
        return url
    else:
        return None

if __name__ == "__main__":
    main()
