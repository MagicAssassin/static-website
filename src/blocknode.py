import re
from enum import Enum
from textnode import *
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str):
    if not block:
        return BlockType.PARAGRAPH

    match = re.findall(r"^#{1,6}\s", block)

    if match:
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    temp_list = block.split("\n")
    quote_check = True
    for i in temp_list:
        if not i.startswith(">"):
            quote_check = False
    
    if quote_check:
        return BlockType.QUOTE
    
    unordered_list_check = True
    for i in temp_list:
        if not i.startswith("- "):
            unordered_list_check = False
    
    if unordered_list_check:
        return BlockType.UNORDERED_LIST

    ordered_list_check = True
    for i in range(len(temp_list)):
        if not temp_list[i].startswith(f"{i+1}. "):
            ordered_list_check = False
    
    if ordered_list_check:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    if markdown:
        new_list=[]

        markdown = markdown.split("\n\n")
        for i in markdown:
            new_list.append(i.strip("\n "))
        
        return new_list

    else:
        return []
