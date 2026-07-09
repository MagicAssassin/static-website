import os, shutil
from textnode import *
from mdtohtml import *
from blocknode import *

def copy_static_folder():
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    list_of_files = os.listdir("static")
    copy_file_to_public("static", "public", list_of_files)

def copy_file_to_public(static_start_path, public_start_path, list_of_files):
    if not os.path.exists("public"):
        os.mkdir("public")
    
    for i in list_of_files:
        static_full_path = os.path.join(static_start_path, i)
        public_full_path = os.path.join(public_start_path, i)
        if os.path.isfile(static_full_path):
            shutil.copy(static_full_path, public_full_path)
        else:
            os.mkdir(public_full_path)
            dir_file_list = os.listdir(static_full_path)
            copy_file_to_public(static_full_path, public_full_path, dir_file_list)

def extract_title(markdown: str):
    if markdown.startswith("# "):
        return markdown[2:]
    else:
        raise Exception("No Title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        from_content = file.read()
    
    with open(template_path, "r") as file:
        template_content = file.read()
    
    html_string = markdown_to_html_node(from_content).to_html()
    the_title = extract_title(markdown=from_content)

    template_content = template_content.replace('{{ Title }}', the_title)
    template_content = template_content.replace('{{ Content }}', html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template_content) 

def main():
    copy_static_folder()
    generate_page("content/index.md","template.html","public/index.html")

main()