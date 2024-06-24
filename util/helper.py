"""
Set of helper functions
"""
import re
from typing import Optional
from models.todo import tag_color_map
from rich.console import Console
from rich.text import Text
from rich.markdown import Markdown


def get_tag_color(category: str) -> str:
    return tag_color_map[category]


def highlight_tag_color(category: str) -> str:
    return format(f"[bold {get_tag_color(category)}]{category}[/bold {get_tag_color(category)}]")


"""Extracts a word with "@" prefix from the end of the string using regex.
  Args:
      {str}: The string to extract the word from.
  Returns:
      {Optional[str]}: The extracted word with "@" prefix if found, otherwise None.
"""


def extract_word_with_at(text: str) -> Optional[str]:
    match = re.search(r'@(\w+)$', text)  # Search for "@" followed by word characters
    if match:
        return match.group(0)  # Return the captured word (group 1)
    else:
        return None


def extract_word_with_colon(text: str) -> Optional[str]:
    words = text.split(":")
    if len(words) == 0 or words[0] == text:
        return None
    return "".join(words[0])


# highlight text with tag
def highlight_text_with_colon(text: str, colon: str) -> Text:
    # Create a Text object with default styling
    default_text = text.replace(colon, "")
    # Highlight the specific word using a custom style
    highlighted_colon = Text(colon, style=f"bold cyan")

    # Combine the default and highlighted parts for rich output
    rich_text = Text("")
    rich_text += highlighted_colon
    rich_text += Text(default_text)
    return rich_text


# highlight text with tag
def highlight_text(pos: int, text: str, tag: Optional[str], status: str) -> Text:
    # Create a Text object with default styling
    default_text = text
    highlighted_tag = Text("")
    if tag is not None:
        default_text = text.replace(tag, "")
        # Highlight the specific word using a custom style
        highlighted_tag = Text(tag, style=f"bold {tag_color_map[tag]}")
    # Assign default text
    rich_text = Text(f"{pos} ")
    rich_text += Text(f"{"❌" if status == "in-progress" else "✅"}  ")
    # add highlighted colon, if present
    colon = extract_word_with_colon(default_text)
    if colon is not None:
        rich_text += highlight_text_with_colon(default_text, colon)
    else:
        rich_text += Text(default_text)
    # add highlighted tag, if present
    if tag is not None:
        rich_text += highlighted_tag
    return rich_text


# TESTING

def test_extract_word_with_at():
    text_01 = "This is a test string with @username"
    result = extract_word_with_at(text_01)
    assert result == "@username"


def text_extract_word_with_at_no_tag():
    text_02 = "No mention of tag here"
    result = extract_word_with_at(text_02)
    assert result is None


if __name__ == "__main__":
    test_extract_word_with_at()
    text_extract_word_with_at_no_tag()
    print("All test cases passed")
