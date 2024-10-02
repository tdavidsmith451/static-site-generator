def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    for b in blocks:
        if b == "":
            continue
        b = b.strip()
        filtered_blocks.append(b)
    return filtered_blocks
        
