from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    print("hello world")
    textNode = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
    print(textNode)

    props_test= {
    "href": "https://www.google.com", 
    "target": "_blank",
    }
    child = HTMLNode("h1", "Title")
    htmlNode = HTMLNode("p", "Testing my code",[child], props_test)
    print(htmlNode)

if __name__ == "__main__":
    main()
