import unittest
from block_to_block_type import *


class TestBlockToBlockType(unittest.TestCase):

    def test_block_to_block_type_para(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_to_block_type_heading(self):
        block = "###This is a heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_block_to_block_type_code(self):
        block = "```\nThis is code\n```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_block_to_block_type_quote(self):
        block = ">This is a quote"
        self.assertEqual(block_to_block_type(block), "quote")

    def test_block_to_block_type_unordered_list(self):
        block = "* This is an\n* unordered list"
        self.assertEqual(block_to_block_type(block), "unordered_list")

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is an\n2. ordered list"
        self.assertEqual(block_to_block_type(block), "ordered_list")

if __name__ == "__main__":
    unittest.main()