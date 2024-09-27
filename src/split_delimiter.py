from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for n in old_nodes:
        if delimiter in n.text:
            split_text = n.text.split(delimiter)
            new_nodes.append(TextNode(split_text[0], n.text_type))
            new_nodes.append(TextNode(split_text[1], text_type))
            new_nodes.append(TextNode(split_text[2], n.text_type))
    return new_nodes


node = TextNode("This is text with a `code block` word", "text")
new_nodes = split_nodes_delimiter([node], "`", "code")
for n in new_nodes:
    print(n.__repr__())