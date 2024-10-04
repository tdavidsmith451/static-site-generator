import unittest
from markdown_to_html_node import *

class TestMarkdownToHTML(unittest.TestCase):

    def test_markdown_to_html(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>")

    def test_paragraph(self):
        markdown = """
Here is a **paragraph**
with a couple lines
of text inside
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><p>Here is a <b>paragraph</b> with a couple lines of text inside</p></div>")

    def test_two_paragraphs(self):
        markdown = """
This test has
multiple paragraphs
within

This is the
second one
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><p>This test has multiple paragraphs within</p><p>This is the second one</p></div>")

    def test_ordered_list(self):
        markdown = """
1. One
2. Two
3. Three
4. Four
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><ol><li>One</li><li>Two</li><li>Three</li><li>Four</li></ol></div>")

    def test_ordered_list(self):
        markdown = """
```
code
```
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.to_html(), "<div><pre><code>code</code></pre></div>")


if __name__ == "__main__":
    unittest.main()