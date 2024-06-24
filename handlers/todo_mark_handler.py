"""
Todo handler for commands
- check
- undo
- renumber
- move
- sort
"""
from typing import Optional, List

from models.messages import LIST_EMPTY_NOTIFICATION, LIST_INDEX_OUT_OF_BOUNDS, TODO_ITEM_CHECKED, TODO_ITEM_UNDO, \
    TODO_ITEMS_RENUMBERED, TODO_ITEMS_MOVE
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


def renumber_todos(display: bool = False, todo_list: List[Todo] = None):
    if todo_list is None:
        todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    # renumber todo items
    try:
        for key, obj in enumerate(todo_list):
            obj['id'] = key + 1
        # persist to file
        write_todo_list_to_file(todo_list)
        return console.print(TODO_ITEMS_RENUMBERED) if display else None
    except IOError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)


def _find_idx_by_property(todo_list: List[Todo], target_idx: int) -> int:
    try:
        found_idx = next(i for i, obj in enumerate(todo_list) if obj['id'] == target_idx)
        return found_idx
    except StopIteration:
        return -1


def move(idx1: int, idx2: int):
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    try:
        src_idx = _find_idx_by_property(todo_list, idx1)
        dst_idx = _find_idx_by_property(todo_list, idx2)
        # bounds check
        if 0 <= src_idx < len(todo_list) and 0 <= dst_idx < len(todo_list):
            temp = todo_list[src_idx]
            todo_list[src_idx] = todo_list[dst_idx]
            todo_list[dst_idx] = temp
            # renumber the todo list and write to file
            renumber_todos(False, todo_list)
            return console.print(TODO_ITEMS_MOVE)
    except IndexError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    except IOError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
