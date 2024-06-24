"""
List of console messages
"""

# list messages
LIST_EMPTY_NOTIFICATION: str = "\n[bold cyan]🏁 There are no todo items. Create a todo list item 🏁[/bold cyan]\n"
LIST_INDEX_OUT_OF_BOUNDS: str = f"[bold red] position index not in todo list !![/bold red]\n"
LIST_COMPLETED_TODOS: str = f"\n[bold purple]✏️ Completed Todos[/bold purple]\n"
LIST_ALL_TODOS: str = f"\n[bold purple]✏️ Todos[/bold purple]\n"
LIST_REMAINING_TODOS: str = f"\n[bold purple]✏️ Remaining Todos[/bold purple]\n"

# add, rm, clear messages
TODO_ITEM_ADDED: str = f"\n [italic cyan] ✏️ added todo item !![/italic cyan]\n"
TODO_ITEM_REMOVED: str = f"\n [italic cyan] ✏️ removed todo item !![/italic cyan]\n"
TODO_ITEMS_CLEAR_PROMPT: str = f"🤔 Are you sure you want to clear todo items?"
TODO_ITEMS_CLEARED: str = f"\n [italic cyan] ✏️ cleared todo items !![/italic cyan]\n"
TODO_ITEMS_CLEAR_ABORT: str = f"\n [italic cyan]  Aborted clearing todo items !![/italic cyan]\n"

# mark messages
TODO_ITEM_CHECKED: str = f"\n [italic cyan] ✏️ todo item completed !![/italic cyan]\n"
TODO_ITEM_UNDO: str = f"\n [italic cyan] ✏️ uncheck todo item !![/italic cyan]\n"
TODO_ITEMS_RENUMBERED: str = f"\n [italic cyan] ✏️ todo items renumbered !![/italic cyan]\n"
