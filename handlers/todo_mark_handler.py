"""
Todo handler for commands
- check
- undo
- renumber
"""
from typing import Optional, List

from models.messages import LIST_EMPTY_NOTIFICATION, LIST_INDEX_OUT_OF_BOUNDS, TODO_ITEM_CHECKED, TODO_ITEM_UNDO, \
    TODO_ITEMS_RENUMBERED
from models.todo import Todo
from util.config import get_todo_list, write_todo_list_to_file
from rich.console import Console

console = Console()


def check_todo_item(pos: int):
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    # guard check
    pos_list = [obj['id'] for obj in todo_list]
    if pos not in pos_list:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    # mark todo item as completed
    try:
        todo_record = next(obj for obj in todo_list if obj['id'] == pos)
        todo_record['status'] = "completed"
        # persist to file
        write_todo_list_to_file(todo_list)
        return console.print(TODO_ITEM_CHECKED)
    except StopIteration:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)


def undo_todo_item(pos: int):
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    # guard check
    pos_list = [obj['id'] for obj in todo_list]
    if pos not in pos_list:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    # mark todo item as in-progress
    try:
        todo_record = next(obj for obj in todo_list if obj['id'] == pos)
        todo_record['status'] = "in-progress"
        # persist to file
        write_todo_list_to_file(todo_list)
        return console.print(TODO_ITEM_UNDO)
    except StopIteration:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)


def renumber_todos():
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    # renumber todo items
    try:
        for key, obj in enumerate(todo_list):
            obj['id'] = key + 1
        # persist to file
        write_todo_list_to_file(todo_list)
        return console.print(TODO_ITEMS_RENUMBERED)
    except IOError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
