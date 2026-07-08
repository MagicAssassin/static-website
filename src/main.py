from textnode import TextNode, TextType

# hello world
print("hello world")

def main():
    text = "This is text with a italic word **bold word**"
    text = text.split("**", maxsplit=2)
    print(text)

main()