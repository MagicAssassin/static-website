class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag: str = tag
        self.value: str = value
        self.children: list[HTMLNode] = children
        self.props: dict = props
    
    def to_html(self):
        raise NotImplementedError("This Method has not been Implemented")
    
    def props_to_html(self):
        the_str = ""
        
        if self.props is None or self.props == {}:
            return ""

        else:
            for i in self.props:
                the_str += f' {i}="{self.props[i]}"'
            
            return the_str

    def __repr__(self):
        return f' HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("TAG IS EMPTY")
        elif self.children is None or self.children == []:
            raise ValueError("THERE IS NO CHILDREN")
        else:
            the_str = f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                the_str += f'{child.to_html()}'
            
            the_str += f'</{self.tag}>'

        return the_str 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        elif self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f' HTMLNode({self.tag}, {self.value}, {self.props})'