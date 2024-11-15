# ai_model.py

class StoryGenerator:
    def __init__(self):
        # Story templates for different genres
        self.templates = {
            "fantasy": "Once upon a time in {setting}, there was a {character} who embarked on a journey filled with {theme}.",
            "sci-fi": "In the year 3025, on the planet {setting}, a {character} discovered {theme}.",
            "comedy": "In the quirky town of {setting}, a {character} hilariously struggled with {theme}.",
        }

    def generate_story(self, genre, character, setting, theme):
        # Use a template if available, otherwise default to a generic format
        template = self.templates.get(genre, "In {setting}, a {character} faced {theme}.")
        return template.format(character=character, setting=setting, theme=theme)

