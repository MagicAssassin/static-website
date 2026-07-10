import os, shutil, sys
from pathlib import Path
from textnode import *
from mdtohtml import *
from blocknode import *

def copy_static_folder():
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    
    list_of_files = os.listdir("static")
    copy_file_to_public("static", "docs", list_of_files)

def copy_file_to_public(static_start_path, public_start_path, list_of_files):
    if not os.path.exists("docs"):
        os.mkdir("docs")
    
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
    markdown_list = markdown.split("\n")
    if markdown_list[0].startswith("# "):
        return markdown_list[0][2:]
    else:
        raise Exception("No Title")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        from_content = file.read()
    
    with open(template_path, "r") as file:
        template_content = file.read()
    
    html_string = markdown_to_html_node(from_content).to_html()
    the_title = extract_title(markdown=from_content)

    template_content = template_content.replace('{{ Title }}', the_title)
    template_content = template_content.replace('{{ Content }}', html_string)
    template_content = template_content.replace('href="/', f'href="{basepath}')
    template_content = template_content.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(template_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    list_of_files = os.listdir(dir_path_content)
    for i in list_of_files:
        full_content_path = os.path.join(dir_path_content, i)
        full_public_path = os.path.join(dest_dir_path, i)
        if os.path.isfile(full_content_path):
            i = Path(i)
            new_file = i.with_suffix(".html")
            full_public_path_html = os.path.join(dest_dir_path, new_file)
            generate_page(from_path=full_content_path, template_path=template_path, dest_path=full_public_path_html, basepath=basepath)
        else:
            os.mkdir(full_public_path)
            generate_pages_recursive(full_content_path, template_path, full_public_path, basepath)

def main():
    all_arguments_list = sys.argv
    if len(all_arguments_list) > 1:
        first_argument = all_arguments_list[1]
    else:
        first_argument = "/"

    print(first_argument)

    copy_static_folder()
    generate_pages_recursive("content", "template.html", "docs", first_argument)
    #generate_page("content/index.md","template.html","public/index.html")
    #generate_page("content/blog/glorfindel/index.md","template.html","public/blog/glorfindel/index.html")
    #generate_page("content/blog/tom/index.md","template.html","public/blog/tom/index.html")
    #generate_page("content/blog/majesty/index.md","template.html","public/blog/majesty/index.html")
    #generate_page("content/contact/index.md","template.html","public/contact/index.html")

main()