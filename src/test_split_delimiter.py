import unittest

from textnode import *
from split_delimiter import *

class TestSplitDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        self.assertEqual(split_nodes_delimiter([node], "`", "code"), [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
            ]
            )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("lets try some text with **Asterisks** as delimiters", "text")
        node2 = TextNode("and then one with more **Asterisks** to delimit", "text")
        self.assertEqual(split_nodes_delimiter([node, node2], "**", "bold"), [
            TextNode("lets try some text with ", "text"),
            TextNode("Asterisks", "bold"),
            TextNode(" as delimiters", "text"),
            TextNode("and then one with more ", "text"),
            TextNode("Asterisks", "bold"),
            TextNode(" to delimit", "text")
        ])

    def test_split_nodes_delimiter_two_words_italic(self):
        node = TextNode('This text has an "italic" word and then another "italic" word', "text")
        self.assertEqual(split_nodes_delimiter([node], '"', "italic"), [
            TextNode("This text has an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and then another ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word", "text")
        ])

if __name__ == "__main__":
    unittest.main()