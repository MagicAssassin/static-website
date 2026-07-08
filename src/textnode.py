from enum import Enum
from htmlnode import *

class TextType(Enum):
    PLAIN = "plain text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, URL=None):
        self.text = text
        self.text_type: TextType = TextType(text_type)
        self.URL = URL
    
    def __eq__(self, other:TextNode):
        if self.text == other.text and self.text_type == other.text_type and self.URL == other.URL:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.URL})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.URL})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src":text_node.URL, "alt":text_node.text})
    else:
        raise Exception("TEXT TYPE IS NOT VALID")
    

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    has_split = False

    if old_nodes:
        for node in old_nodes:
            if node.text_type == TextType.PLAIN:
                text_list = node.text.split(delimiter, maxsplit=2)
                if len(text_list) == 3:
                    has_split = True
                    new_nodes.append(TextNode(text_list[0], text_type=TextType.PLAIN))
                    new_nodes.append(TextNode(text_list[1], text_type=text_type))
                    if text_list[2] != "":
                        new_nodes.append(TextNode(text_list[2], text_type=TextType.PLAIN))
                elif len(text_list) == 1:
                    new_nodes.append(node)
                else:
                    raise Exception("NO CLOSING DELIMETER")
                
            else:
                new_nodes.append(node)
        
        if has_split:
            return split_nodes_delimiter(new_nodes, delimiter, text_type)
        else:
            return new_nodes

    else:
        return []


























    