"""
Todo handler for commands
- ls all
- ls done
- ls
"""
from models.messages import LIST_EMPTY_NOTIFICATION, LIST_COMPLETED_TODOS, LIST_REMAINING_TODOS, LIST_ALL_TODOS
from util.config import get_todo_list
from typing import List
from models.todo import Todo
from rich.console import Console
from rich.text import Text

from util.helper import highlight_text

console = Console()


# print todo items on console
def print_todo_items(todo_list: List[Todo]):
    output = Text("")
    for item in todo_list:
        output += highlight_text(item)
        output += Text("\n")
    console.print(output)


def list_completed_todo_items():
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        console.print(LIST_EMPTY_NOTIFICATION)
    else:
        todo_list = [obj for obj in todo_list if obj['status'] == "completed"]
        console.print(LIST_COMPLETED_TODOS)
        print_todo_items(todo_list)


# list pending todo items
def list_pending_todo_items():
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        console.print(LIST_EMPTY_NOTIFICATION)
    else:
        todo_list = [obj for obj in todo_list if obj['status'] == "in-progress"]
        console.print(LIST_REMAINING_TODOS)
        print_todo_items(todo_list)


# list all todo items
def list_all_todo_items():
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        console.print(LIST_EMPTY_NOTIFICATION)
    else:
        console.print(LIST_ALL_TODOS)
        print_todo_items(todo_list)
