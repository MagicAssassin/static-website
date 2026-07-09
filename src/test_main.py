import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from main import extract_title

class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")    

if __name__ == "__main__":
    unittest.main()