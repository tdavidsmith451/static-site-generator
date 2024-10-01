import unittest
from extract_links import *

class TestExtractLinks(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_images_2(self):
        text = "This time there is only one link: ![dog](https://i.pictureofadog.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("dog", "https://i.pictureofadog.jpeg")])

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        print(extract_markdown_links(text))
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_extract_markdown_images_no_image(self):
        text = "This is text"
        self.assertEqual(extract_markdown_images(text), [])

if __name__ == "__main__":
    unittest.main()