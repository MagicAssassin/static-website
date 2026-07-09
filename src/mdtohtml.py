from textnode import *
from htmlnode import *
from blocknode import *

def markdown_to_html_node(markdown):
    list_of_blocks = markdown_to_blocks(markdown=markdown)
    md_parent_nodes = []

    for block in list_of_blocks:
        block_type = block_to_block_type(block=block)

        if block_type == BlockType.HEADING:

            heading_type: int = determin_heading_type(block)
            block = block[heading_type+1:]

            list_of_inline_html_node = text_to_childrent_html_node_list(block)
            parent_node = ParentNode(tag=f"h{heading_type}", children=list_of_inline_html_node)
            md_parent_nodes.append(parent_node)
        
        elif block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            list_of_inline_html_node = text_to_childrent_html_node_list(block)
            parent_node = ParentNode(tag="p", children=list_of_inline_html_node)
            md_parent_nodes.append(parent_node)
        
        elif block_type == BlockType.CODE:
            block = block[4:-3]
            child_node = LeafNode(tag="code", value=block)
            parent_node = ParentNode(tag="pre", children=[child_node])
            md_parent_nodes.append(parent_node)
        
        elif block_type == BlockType.QUOTE:
            paragraph_node_list = quote_helper(block=block)
            parent_node = ParentNode(tag="blockquote", children=paragraph_node_list)
            md_parent_nodes.append(parent_node)
        
        elif block_type == BlockType.UNORDERED_LIST:
            li_node_list = list_helper(block, BlockType.UNORDERED_LIST)
            parent_node = ParentNode(tag="ul", children=li_node_list)
            md_parent_nodes.append(parent_node)
        
        elif block_type == BlockType.ORDERED_LIST:
            li_node_list = list_helper(block, BlockType.ORDERED_LIST)
            parent_node = ParentNode(tag="ol", children=li_node_list)
            md_parent_nodes.append(parent_node)
        
        else:
            raise Exception("Somthing Went Wrong when getting the block type")

    return ParentNode(tag="div", children=md_parent_nodes)



def text_to_childrent_html_node_list(text):
    text_node_list = text_to_textnodes(text=text)
    chid_node_list = []
    for text_node in text_node_list:
        child_html_node = text_node_to_html_node(text_node=text_node)
        chid_node_list.append(child_html_node)
    return chid_node_list

def determin_heading_type(text: str) -> int:
    if text.startswith("# "):
        return 1
    elif text.startswith("## "):
        return 2
    elif text.startswith("### "):
        return 3
    elif text.startswith("#### "):
        return 4
    elif text.startswith("##### "):
        return 5
    elif text.startswith("###### "):
        return 6
    else:
        raise Exception("INVALID HEADING TYPE")

def quote_helper(block):
    list_of_inline_text = block.split("\n")
    p_list_nodes = []
    for inline_text in list_of_inline_text:
        inline_text = inline_text[1:]
        list_of_inline_html_node = text_to_childrent_html_node_list(inline_text)
        paragraph_node = ParentNode(tag="p", children=list_of_inline_html_node)
        p_list_nodes.append(paragraph_node)
    
    return p_list_nodes

def list_helper(block, list_type):
    if list_type == BlockType.UNORDERED_LIST:
        indicator = 2
    else:
        indicator = 3
    list_of_inline_text = block.split("\n")
    li_item_nodes = []
    for inline_text in list_of_inline_text:
        inline_text = inline_text[indicator:]
        list_of_inline_html_node = text_to_childrent_html_node_list(inline_text)
        li_node = ParentNode(tag="li", children=list_of_inline_html_node)
        li_item_nodes.append(li_node)
    
    return li_item_nodes