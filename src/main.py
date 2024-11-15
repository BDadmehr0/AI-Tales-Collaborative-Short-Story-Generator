# main.py

from src.ai_model import StoryGenerator

def main():
    print("🌟 Welcome to AI Tales: Collaborative Short Story Generator 🌟")
    print("Let's create a story together! 🎨")

    # Initialize the AI story generator
    generator = StoryGenerator()

    # Get user input
    genre = input("Choose a genre (e.g., fantasy, sci-fi, comedy): ").strip().lower()
    character = input("Describe your main character: ").strip()
    setting = input("Where does the story take place? ").strip()
    theme = input("What's the main theme of the story? (e.g., adventure, love, revenge): ").strip()

    # Generate the story
    print("\nGenerating your story... 🎉\n")
    story = generator.generate_story(genre, character, setting, theme)

    # Display the story
    print("Here’s your story:\n")
    print(story)

if __name__ == "__main__":
    main()

