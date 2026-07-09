import unittest
from textnode import *
from htmlnode import *
from blocknode import *

class TestTextNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_block_to_block_type_heading1(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.HEADING)
    
    def test_block_to_block_type_heading2(self):
        block = "###### This is a heading"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading3(self):
        block = "#This is a heading"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_heading4(self):
        block = "####### This is a heading"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_heading5(self):
        block = "This is a heading ######"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_code1(self):
        block = "```\nThis is a heading```"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_code2(self):
        block = "```\nThis is a heading\n```"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_code3(self):
        block = "```\nThis is a heading``"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_code4(self):
        block = "```This is a heading```"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_code5(self):
        block = "``\nThis is a heading```"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_quote1(self):
        block = ">This is the First Line\n> This is the Secondline"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.QUOTE)
    
    def test_block_to_block_type_quote2(self):
        block = ">This is the First Line\n< This is the Secondline"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_unordered_list1(self):
        block = "- This is the first line\n- This is the second line"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_block_to_block_type_unordered_list2(self):
        block = "- This is the first line\n-This is the second line"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_unordered_list3(self):
        block = "- This is the first line\nThis is the second line"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_ordered_list1(self):
        block = "1. This is the first line\n2. This is the second line\n3. This is the third line"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.ORDERED_LIST)
    
    def test_block_to_block_type_ordered_list2(self):
        block = "1. This is the first line\n1. This is the second line\n3. This is the third line"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_ordered_list3(self):
        block = "1.This is the first line\n2. This is the second line\n3. This is the third line"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)
    
    def test_block_to_block_type_ordered_list1(self):
        block = "This is is a very very very very long paragraph"
        block_type = block_to_block_type(block=block)

        self.assertEqual(block_type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()