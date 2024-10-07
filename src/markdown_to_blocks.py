def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    for b in blocks:
        if b == "":
            continue
        b = b.strip()
        filtered_blocks.append(b)
    return filtered_blocks
        
def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ").strip()
        else:
            raise Exception("no header found")