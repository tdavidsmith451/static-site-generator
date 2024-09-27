from htmlnode import *
from textnode import TextNode
from textnode_to_htmlnode import *
import unittest

class TestTextNodeToHTML(unittest.TestCase):

    def test_text_node_to_html_node(self):
        node = TextNode("this is bold text", "bold")
        self.assertEqual(text_node_to_html_node(node), LeafNode("b", "this is bold text"))

    def test_text_node_to_html_node_2(self):
        node = TextNode("this is italic text", "italic")
        self.assertEqual(text_node_to_html_node(node), LeafNode("i", "this is italic text"))

    def test_text_node_to_html_node_3(self):
        node = TextNode("this is alt text", "image", "www.url.com")
        self.assertEqual(text_node_to_html_node(node), LeafNode("img", "", {"src": "www.url.com", "alt": "this is alt text"}))


if __name__ == "__main__":
    unittest.main()