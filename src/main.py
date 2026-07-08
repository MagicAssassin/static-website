from textnode import TextNode, TextType

# hello world
print("hello world")

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))

main()