"""
List todo items handler
"""
from util.config import parse_file
from typing import Optional, List
from models.todo import Todo
from rich import console
from rich.text import Text

from util.helper import highlight_text, extract_word_with_colon, highlight_text_with_colon

console = console.Console()


def get_todo_list() -> Optional[List[Todo]]:
    data = parse_file()
    if data is not None:
        return data.get('todos')
    return None

# highlight with tag


# list pending todo items
def list_pending_todo_items():
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        console.print(f"\n [bold cyan]🏁 There are no todo items. Create a todo list item 🏁[/bold cyan]\n")
    else:
        output = Text("")
        for item in todo_list:
            output += Text("\n")
            output += highlight_text(item['id'], item['desc'], item['tag'], item['status'])
        console.print(output)

