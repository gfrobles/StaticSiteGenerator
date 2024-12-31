from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag present")
        if self.children == None:
            raise ValueError("No children present")
        
        html = ""
        for child in self.children:
            html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"