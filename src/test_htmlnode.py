from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("p", "howdy", None, {"href":"https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_2(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_3(self):
        node = HTMLNode("h", "booyah", None, {"key1":"www.value1.com", "key2":"www.value2.com"})
        self.assertEqual(node.props_to_html(), ' key1="www.value1.com" key2="www.value2.com"')
        
class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("p", "yeehaw")
        self.assertEqual(node.to_html(), "<p>yeehaw</p>")

    def test_to_html_2(self):
        node = LeafNode("a", "When I was a young warthog...", {"key": "value"})
        self.assertEqual(node.to_html(), '<a key="value">When I was a young warthog...</a>')

    def test_to_html_3(self):
        node = LeafNode(None, "This test has a value and nothing else")
        self.assertEqual(node.to_html(), "This test has a value and nothing else")

class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ], {"key": "value"}
        )
        self.assertEqual(node.to_html(), '<p key="value"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_2(self):
        node = ParentNode(
            "p",
            [
                ParentNode("e",
                            [LeafNode("g", "G text"),
                             LeafNode("z", "Z text")]),
                LeafNode("b", "Bold text"),
                LeafNode("i", "italictext"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><e><g>G text</g><z>Z text</z></e><b>Bold text</b><i>italictext</i></p>')

    def test_to_html_3(self):
        node = ParentNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()