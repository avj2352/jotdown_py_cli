import typer
from typing_extensions import Annotated
from typing import Optional
from rich.console import Console
# ..custom
from util.config import create_file_if_not_exists
from handlers import todo_list_handler, todo_add_handler

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
    todo_add_handler.add_todo_item(text=text)


# check
@app.command(short_help="mark todo item by index as completed")
def check(pos: int):
    typer.echo(f"mark todo item by index as completed")


# undo
@app.command(short_help="mark status as in progress for task by position")
def undo(pos: int):
    typer.echo(f"undo last todo item status")


# mv
@app.command(short_help="move task items from source to destination")
def mv(src: int, dst: int):
    typer.echo(f"move task items from source to destination")


# rm
@app.command(short_help="remove todo item by position")
def rm(pos: int):
    typer.echo(f"remove todo item by position")


# clear
@app.command(short_help="clear todo items")
def clear():
    typer.echo(f"clear todo items")


# sort
@app.command(short_help="sort todo items by tags")
def sort():
    typer.echo(f"sort todo items by tags")


# about
# @app.command(short_help="mark todo item by index as done")
# def help():
#     typer.echo()

if __name__ == "__main__":
    app_init()
    app()
