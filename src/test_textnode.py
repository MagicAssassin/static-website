import unittest
from textnode import *
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)
        
    
    def test_not_eq_1(self):
        node3 = TextNode("This is a text node", TextType.IMAGE)
        node4 = TextNode("This is a text node", TextType.ITALIC)

        self.assertNotEqual(node4,node3)
    
    def test_not_eq_2(self):
        node3 = TextNode("This is a text node", TextType.IMAGE, "www.boot.dev")
        node4 = TextNode("This is a text node", TextType.IMAGE)

        self.assertNotEqual(node4,node3)
    
    def test_text_1(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_3(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_4(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_5(self):
        node = TextNode("This is a text node", TextType.LINK, URL="www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "www.boot.dev"})
    
    def test_text_6(self):
        node = TextNode("This is a text node", TextType.IMAGE, URL="www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.boot.dev", "alt":"This is a text node"})

if __name__ == "__main__":
    unittest.main()