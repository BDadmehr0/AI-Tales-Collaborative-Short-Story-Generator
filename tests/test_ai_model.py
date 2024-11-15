# test_ai_model.py

import unittest
from src.ai_model import StoryGenerator

class TestStoryGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = StoryGenerator()

    def test_generate_story_fantasy(self):
        story = self.generator.generate_story("fantasy", "brave knight", "enchanted forest", "finding a lost artifact")
        self.assertIn("enchanted forest", story)
        self.assertIn("brave knight", story)
        self.assertIn("finding a lost artifact", story)

    def test_generate_story_sci_fi(self):
        story = self.generator.generate_story("sci-fi", "curious astronaut", "Mars", "uncovering alien technology")
        self.assertIn("Mars", story)
        self.assertIn("curious astronaut", story)
        self.assertIn("uncovering alien technology", story)

    def test_generate_story_default(self):
        story = self.generator.generate_story("unknown", "mysterious stranger", "abandoned city", "solving a mystery")
        self.assertIn("abandoned city", story)
        self.assertIn("mysterious stranger", story)
        self.assertIn("solving a mystery", story)

if __name__ == "__main__":
    unittest.main()

