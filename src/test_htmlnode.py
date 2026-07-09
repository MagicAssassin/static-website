import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_probs_to_html_1(self):
        node_1 = HTMLNode("h1", "This is a text", [], {"href": "https://www.google.com", "target": "_blank",})
        the_str= ' href="https://www.google.com" target="_blank"'

        self.assertEqual(the_str, node_1.props_to_html())
    
    def test_probs_to_html_2(self):
        node_1 = HTMLNode("h1", "This is a text", [], {})
        the_str= ''

        self.assertEqual(the_str, node_1.props_to_html())
    
    def test_probs_to_html_3(self):
        node_1 = HTMLNode("h1", "This is a text", [], {"href": "https://www.google.com", "target": "_blank",})
        the_str= ''

        self.assertNotEqual(the_str, node_1.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node_2 = LeafNode(tag=None, value="grandchild")
        child_node = ParentNode("span", [grandchild_node, grandchild_node_2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b>grandchild</span></div>",
        )
        
    
    

if __name__ == "__main__":
    unittest.main()