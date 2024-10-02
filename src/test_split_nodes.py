import unittest
from textnode import *
from extract_links import *
from split_nodes import *

class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_image(self):
        node =  TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", "text")
        self.assertEqual(split_nodes_image([node]),[
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_split_nodes_image_2(self):
        node = TextNode("This text has three images ![dog](https://i.pictureofadog.com)![cat](https://i.pictureofacat.com)![frog](https://i.pictureofafrog.com)", "text")
        self.assertEqual(split_nodes_image([node]),[
            TextNode("This text has three images ", "text"),
            TextNode("dog", "image", "https://i.pictureofadog.com"),
            TextNode("cat", "image", "https://i.pictureofacat.com"),
            TextNode("frog", "image", "https://i.pictureofafrog.com")
        ])

    def test_split_nodes_image_no_images(self):
        node = TextNode("no images", "text")
        self.assertEqual(split_nodes_image([node]), [
            TextNode("no images", "text")
        ])

    def test_split_nodes_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text)
        self.assertEqual(split_nodes_link([node]), [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev")
        ])

if __name__ == "__main__":
    unittest.main()