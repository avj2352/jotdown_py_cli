import typer
from typing_extensions import Annotated
from typing import Optional
from rich.console import Console
# ..custom
from util.config import create_file_if_not_exists
from handlers import todo_list_handler, todo_add_handler
from util.helper import extract_word_with_at

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
        typer.echo(f"list all todo items")
    elif arg == "done":
        typer.echo(f"list done todo items")
    else:
        todo_list_handler.list_pending_todo_items()


# add
@app.command(short_help="add todo item")
def add(text: str):
    tag = extract_word_with_at(text)
    todo_add_handler.add_todo_item(text=text, tag=tag)


# check
@app.command(short_help="mark todo item by index as done")
def check(pos: int):
    typer.echo(f"mark todo item by index as done")


# undo
@app.command(short_help="mark status as in progress for task by position")
def undo():
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
def clear(arg: str = None):
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
