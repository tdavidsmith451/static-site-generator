import re


def extract_markdown_images(text):
    alt_url_list = []
    alt_text = re.findall(r"(?<=\!\[).*?(?=\])", text)
    url = re.findall(r"(?<=\()http.*?(?=\))", text)
    for i in range(0, len(alt_text)):
        tuple = (alt_text[i], url[i])
        alt_url_list.append(tuple)
    return alt_url_list

def extract_markdown_links(text):
    anchor_url_list = []
    anchor_text = re.findall(r"(?<=\[).*?(?=\]\(http)", text)
    url = re.findall(r"(?<=\()http.*?(?=\))", text)
    for i in range(0, len(anchor_text)):
        tuple = (anchor_text[i], url[i])
        anchor_url_list.append(tuple)
    return anchor_url_list