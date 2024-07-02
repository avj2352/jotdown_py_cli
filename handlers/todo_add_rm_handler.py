"""
Todo handler for commands
- add
- rm
- clear
- update
- tag
"""
from models.messages import TODO_ITEM_ADDED, LIST_EMPTY_NOTIFICATION, LIST_INDEX_OUT_OF_BOUNDS, TODO_ITEM_REMOVED, \
    TODO_ITEMS_CLEARED, TODO_ITEM_DESC_UPDATED, TODO_ITEM_TAG_UPDATED
from util.config import write_todo_list_to_file
from typing import Optional, List
from models.todo import Todo
from datetime import datetime
from rich import console
from handlers.todo_list_handler import get_todo_list
from util.helper import extract_word_with_at, extract_description

console = console.Console()


def add_todo_item(text: str):
    tag: Optional[str] = extract_word_with_at(text)
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
    console.print(TODO_ITEM_ADDED)


def remove_todo_item(pos: int):
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    # guard check
    pos_list = [obj['id'] for obj in todo_list]
    if pos not in pos_list:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    # remove todo item
    filtered_list = [obj for obj in todo_list if obj['id'] != pos]
    try:
        # persist to file
        write_todo_list_to_file(filtered_list)
        return console.print(TODO_ITEM_REMOVED)
    except IOError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)


def clear_todo_items():
    try:
        # persist to file
        write_todo_list_to_file([])
        return console.print(TODO_ITEMS_CLEARED)
    except IOError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)


def update_todo_description(pos: int, text: str):
    # empty list check
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    # guard check
    pos_list = [obj['id'] for obj in todo_list]
    if pos not in pos_list:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    try:
        todo_record = next(obj for obj in todo_list if obj['id'] == pos)
        curr_tag = todo_record['tag']
        todo_record['desc'] = text
        if curr_tag is not None or curr_tag != "":
            todo_record['desc'] += " "
            todo_record['desc'] += curr_tag
        # persist to file
        write_todo_list_to_file(todo_list)
        return console.print(TODO_ITEM_DESC_UPDATED)
    except StopIteration:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    except IOError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)


def change_tag_annotation(pos: int, tag: str):
    # empty list check
    todo_list: List[Todo] = get_todo_list()
    if todo_list is None or len(todo_list) == 0:
        return console.print(LIST_EMPTY_NOTIFICATION)
    # guard check
    pos_list = [obj['id'] for obj in todo_list]
    if pos not in pos_list:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    try:
        todo_record = next(obj for obj in todo_list if obj['id'] == pos)
        curr_desc = extract_description(todo_record['desc'])
        if curr_desc is not None or curr_desc != "":
            todo_record['desc'] = curr_desc
            todo_record['desc'] += " "
            todo_record['desc'] += tag
            todo_record['tag'] = tag
        # persist to file
        write_todo_list_to_file(todo_list)
        return console.print(TODO_ITEM_TAG_UPDATED)
    except StopIteration:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
    except IOError:
        return console.print(LIST_INDEX_OUT_OF_BOUNDS)
