from textnode import *
from split_nodes import *
from split_delimiter import *

delimiters = {"`": "code", "**": "bold",'*': "italic"}

def text_to_textnodes(text):
    original_node = TextNode(text, "text")
    split_by_d = [original_node]
    for delimiter, type in delimiters.items():
        split_by_d = split_nodes_delimiter(split_by_d, delimiter, type)
    split_by_images =split_nodes_image(split_by_d)
    textnodes = split_nodes_link(split_by_images)
    return textnodes



text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
print(text_to_textnodes(text))