from textnode import *


def main():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    matches = extract_markdown_links(text)
    print(matches)
    text = text.split(f"[{matches[0][0]}]({matches[0][1]})", 1)

    print(text)

main()