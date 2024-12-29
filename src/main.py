from textnode import TextType, TextNode

def main():
    print("hello world")
    textNode = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
    print(textNode)

if __name__ == "__main__":
    main()
