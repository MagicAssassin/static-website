import re
from textnode import *


def main():
    md = '''1. This sadkjhd
2. Another Item
3. Third Item'''

    temp_list = md.split("\n")
    quote_check = True
    print(temp_list)
    for i in range(len(temp_list)):
        print(temp_list[i])
        if not temp_list[i].startswith(f"{i+1}. "):
            quote_check = False
    
    print(quote_check)


main()