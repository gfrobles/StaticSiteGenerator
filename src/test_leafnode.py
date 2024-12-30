import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_p_to_html(self):
        lead_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(lead_node.to_html(),"<p>This is a paragraph of text.</p>")

    def test_a_to_html(self):
        lead_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(lead_node.to_html(),'<a href="https://www.google.com">Click me!</a>')