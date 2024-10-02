from textnode import *
from extract_links import *

def split_nodes_image(old_nodes):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != "text":
            new_nodes.append(n)
            continue
        alt_url_list = extract_markdown_images(n.text)
        if alt_url_list == []:
            new_nodes.append(n)
            continue
        text = n.text
        for m in alt_url_list:
            alt = m[0]
            url = m[1]
            split_text = text.split(f'![{alt}]({url})', 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] == "":
                new_nodes.append(TextNode(alt, 'image', url))
                del split_text[0]
                text = split_text[0]
                continue
            new_nodes.append(TextNode(split_text.pop(0), "text"))
            new_nodes.append(TextNode(alt, 'image', url))                 
            text = split_text[0]
        if text != "":
            new_nodes.append(TextNode(text, "text"))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != "text":
            new_nodes.append(n)
            continue
        anchor_url_list = extract_markdown_links(n.text)
        if anchor_url_list == []:
            new_nodes.append(n)
            continue
        text = n.text
        for m in anchor_url_list:
            anchor = m[0]
            url = m[1]
            split_text = text.split(f'[{anchor}]({url})', 1)
            if len(split_text) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if split_text[0] == "":
                new_nodes.append(TextNode(anchor, 'link', url))
                del split_text[0]
                text = split_text[0]
                continue
            new_nodes.append(TextNode(split_text.pop(0), "text"))
            new_nodes.append(TextNode(anchor, 'link', url))                 
            text = split_text[0]
        if text != "":
            new_nodes.append(TextNode(text, "text"))
    return new_nodes
