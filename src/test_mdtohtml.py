import unittest
from textnode import *
from htmlnode import *
from blocknode import *
from mdtohtml import *

class TestTextNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_headblock_1(self):
        md = "###### This is a **BOLD HEADING** thank you"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is a <b>BOLD HEADING</b> thank you</h6></div>",
        )
    
    def test_headblock_2(self):
        md = "# This is a **BOLD HEADING** thank you"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a <b>BOLD HEADING</b> thank you</h1></div>",
        )
    
    def test_quote(self):
        md = "> This is a QUOTE\n>This is another QUOTE"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a QUOTE\nThis is another QUOTE</blockquote></div>",
        )
    
    def test_ordered_list(self):
        md = "1. This is number 1\n2. This is number 2"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is number 1</li><li>This is number 2</li></ol></div>",
        )
    
    def test_unordered_list(self):
        md = "- This is number 1\n- This is number 2"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is number 1</li><li>This is number 2</li></ul></div>",
        )
    
    def test_big_markdown(self):
        md = """
## This is **bolded heading**

This is some random paragraph that has _italic text_

- first
- second

This is another paragraph with [link](www.boot.dev) and ![image](somthing) plus **bold** with _italic_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h2>This is <b>bolded heading</b></h2><p>This is some random paragraph that has <i>italic text</i></p><ul><li>first</li><li>second</li></ul><p>This is another paragraph with <a href="www.boot.dev">link</a> and <img src="somthing" alt="image"></img> plus <b>bold</b> with <i>italic</i></p></div>',
        )

if __name__ == "__main__":
    unittest.main()