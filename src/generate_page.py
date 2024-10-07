from markdown_to_html_node import *
from htmlnode import *
from markdown_to_blocks import *
import os


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = open(from_path).read()
    html_template = open(template_path).read()

    html_string = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    html_page = html_template.replace(r"{{ Title }}", title).replace(r"{{ Content }}", html_string)

    with open(dest_path, "w") as index:
        index.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, entry)
        if os.path.isfile(path):
            if entry.endswith(".md"):
                generate_page(path, template_path, f"{dest_dir_path}/index.html")
            else:
                continue
        if os.path.isdir(path):
            new_dir_path = os.path.join(dest_dir_path, entry)
            os.mkdir(new_dir_path)
            generate_pages_recursive(path, template_path, new_dir_path)






