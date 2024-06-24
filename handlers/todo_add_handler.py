"""
Add todo command handler
"""

from util.config import write_todo_list_to_file
from typing import Optional, List
from models.todo import Todo
from datetime import datetime
from rich import console
from handlers.todo_list_handler import get_todo_list

console = console.Console()


def add_todo_item(text: str, tag: Optional[str]):
    todo_list = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        todo_list: List[Todo] = []
        record = Todo(id=1, desc=text, tag=tag, status="in-progress", modified=datetime.now().isoformat())
        todo_list.append(record)
    elif len(todo_list) > 0:
        record = Todo(id=len(todo_list) + 1, desc=text, tag=tag, status="in-progress",
                      modified=datetime.now().isoformat())
        todo_list.append(record)
    # write to file
    write_todo_list_to_file(todo_list)
    console.print(f"\n [italic cyan] ✏️ added todo item !![/italic cyan]\n")
