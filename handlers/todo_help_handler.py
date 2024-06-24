"""
Todo handler for commands
- about
- help (overwrite)
"""

HELP_TEXT: str = """
       __      __      __
      / /___  / /_____/ /___ _      ______
 __  / / __ \/ __/ __  / __ \ | /| / / __ \
/ /_/ / /_/ / /_/ /_/ / /_/ / |/ |/ / / / /
\____/\____/\__/\__,_/\____/|__/|__/_/ /_/
✨ Jotdown CLI, v1.0.0. A modern command line Todo application with colorized annotation, written using Python click ✨
"""

def about():
    return HELP_TEXT
