import unittest

from textnode import *
from split_delimiter import *

class TestSplitDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        self.assertEqual(split_nodes_delimiter([node], "`", "code"), [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
            ]
            )




if __name__ == "__main__":
    unittest.main()