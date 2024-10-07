import unittest
from markdown_to_blocks import *

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(markdown_to_blocks(markdown), ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"])

    def test_markdown_to_blocks_empty(self):
        markdown = ""
        self.assertEqual(markdown_to_blocks(markdown), [])

    def test_extract_title(self):
        markdown = "# Heading "
        self.assertEqual(extract_title(markdown), "Heading")



if __name__ == "__main__":
    unittest.main()