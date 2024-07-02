import typer
from typing_extensions import Annotated
from typing import Optional
from rich.console import Console

from models.messages import TODO_ITEMS_CLEAR_PROMPT, TODO_ITEMS_CLEAR_ABORT
# ..custom
from util.config import create_file_if_not_exists
from handlers import todo_list_handler, todo_add_rm_handler, todo_mark_handler, todo_help_handler

# init console and typer
console = Console()
app = typer.Typer()


# init function
def app_init():
    create_file_if_not_exists()


# ls
@app.command(short_help="list todo items")
def ls(arg: Annotated[Optional[str], typer.Argument(help=f"list todo items - all | done | NONE")] = None):
    if arg == "all":
        todo_list_handler.list_all_todo_items()
    elif arg == "done":
        todo_list_handler.list_completed_todo_items()
    else:
        todo_list_handler.list_pending_todo_items()


# add
@app.command(short_help="add todo item")
def add(text: Annotated[str, typer.Argument(help=f"todo item description")]):
    todo_add_rm_handler.add_todo_item(text=text)


# check
@app.command(short_help="mark todo item by index as completed")
def check(pos: Annotated[int, typer.Argument(help=f"todo item number or position")]):
    todo_mark_handler.check_todo_item(pos)


# undo
@app.command(short_help="mark status as in progress for task by position")
def undo(pos: Annotated[int, typer.Argument(help=f"todo item number or position")]):
    todo_mark_handler.undo_todo_item(pos)


# mv
@app.command(short_help="move task items from source to destination")
def mv(src: Annotated[int, typer.Argument(help=f"source position")],
       dst: Annotated[int, typer.Argument(help=f"destination position")]):
    todo_mark_handler.move(src, dst)


# rm
@app.command(short_help="remove todo item by position")
def rm(pos: Annotated[int, typer.Argument(help=f"todo item number or position")]):
    todo_add_rm_handler.remove_todo_item(pos)


# clear
@app.command(short_help="clear todo items")
def clear():
    clear_todos = typer.confirm(TODO_ITEMS_CLEAR_PROMPT)
    if not clear_todos:
        raise typer.Abort()
    todo_add_rm_handler.clear_todo_items()


# renumber todo items
@app.command(short_help="renumber todo items' position")
def renumber():
    todo_mark_handler.renumber_todos(display=True)


# sort todo items
@app.command(short_help="sort todo items by tags")
def sort():
    todo_mark_handler.sort_todos()


# about todo cli
@app.command(short_help="about the application")
def about():
    text = todo_help_handler.about()
    console.print(text)


@app.command(short_help="update todo description")
def update(pos: Annotated[int, typer.Argument(help=f"todo item number or position")],
           desc: Annotated[str, typer.Argument(help=f"todo item new description")]):
    todo_add_rm_handler.update_todo_description(pos=pos, text=desc)


@app.command(short_help="add/change tag annotation of a particular todo item")
def tag(pos: Annotated[int, typer.Argument(help=f"todo item number or position")],
        annotate: Annotated[str, typer.Argument(help=f"new tag annotation")]):
    todo_add_rm_handler.change_tag_annotation(pos=pos, tag=annotate)


if __name__ == "__main__":
    app_init()
    app()
