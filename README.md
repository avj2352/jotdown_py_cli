# 🐍️ Jotdown-Py - Todo CLI app using Python Typer

Jotdown CLI, `v1.0.0`. A modern command line Todo application with colorized annotations, written using Python & Typer

![version](https://img.shields.io/badge/version-1.0.0-blue)
- Link to the original CLI built using Rust - [Click here](https://github.com/avj2352/jotdown_rust_cli)
- A modern Todo application with extra features!

Jotdown version `1.0.0` CLI features -

```bash
 jd: Jotdown
       __      __      __                  
      / /___  / /_____/ /___ _      ______ 
 __  / / __ \/ __/ __  / __ \ | /| / / __ \
/ /_/ / /_/ / /_/ /_/ / /_/ / |/ |/ / / / /
\____/\____/\__/\__,_/\____/|__/|__/_/ /_/ 
                                           
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          "Install completion for the current shell."                                                                                             │
│ --show-completion             "Show completion for the current shell, to copy it or customize the installation."                                                      │
│ --help                        "Show this message and exit."                                                                                                           │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ about      "about the application"                                                                                                                                    │
│ add        "add todo item"                                                                                                                                            │
│ check      "mark todo item by index as completed"                                                                                                                     │
│ clear      "clear todo items"                                                                                                                                         │
│ ls         "list todo items"                                                                                                                                          │
│ mv         "move task items from source to destination"                                                                                                               │
│ renumber   "renumber todo items position"                                                                                                                            │
│ rm         "remove todo item by position"                                                                                                                             │
│ sort       "sort todo items by tags"                                                                                                                                  │
│ undo       "mark status as in progress for task by position"                                                                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

  Environment variables:    
    JOTDOWN_DB_PATH=./jotdown.json  Specify DB path [default: <project_root>/.jotdown-db.json]
```

## Emojis Used

The following emojis were used in the project - 🏁 |  ✅ | ✏️ | ❌ | 🤔 | ✨ 

## 🚨 RELEASE v1.0.0 available

- Release executable `v1.1.0` available under `dist` folder.
- Copy the executable or run the shell script `build_release.sh`
- to generate the latest build (warning: using the shell script, generates a canary build)

## Important Links
- [Original Jotdown CLI using Rust](https://github.com/avj2352/jotdown_rust_cli)
- [Typer Python CLI](https://typer.tiangolo.com/tutorial/)
- [Rich - Python color console](https://github.com/Textualize/rich)
- [Python - JSON serde dataclass - jsonpickle](https://jsonpickle.github.io)
- [Python - PyInstaller - creating an executable](https://pyinstaller.org/en/stable/)

## NOTE: About the file - .jotdown-db.json

Jotdown remembers your tasks, todos and reminders by persisting them under `<your_project_root>/.jotdown-db.json`
The default store of the JSON file is in $HOME location. This could vary based on the operating system:

> In the upcoming release 1.2.0 you can configure your own path to store `.jotdown-db.json`, by setting the env variable

```bash
# set datastore path
JOTDOWN_DB_PATH=~/Dropbox/jotdown.json  Specify DB path [default: $HOME/.jotdown-db.json]
```

## Run (using Typer)

To run jotdown as a cli app using Python Typer command

```bash
python main.py --help
```

````
## Data structure (jotdown-db.json)

Typically structure of a `todo-db.json`

> NOTE: in `todo` the position of the element within the HashMap is the order in the UI

```json
{
  "tags": ["important", "today", "week"],
  "todos": [
    {
      "id": 1,
      "desc": "HOME: Buy groceries for the week @today",
      "status": "pending",
      "modified": "2023-09-25T13:00:04.792Z"
    }
  ]
}
````

# Creating a Python executable

Creating a distributable executable for a Typer application using PyInstaller involves a few steps:

1. Project Setup:

Ensure you have Python and PyInstaller installed. You can install them using pip install python3 pyinstaller.
Create a project directory for your Typer application with your main script (e.g., main.py) containing your Typer definitions and logic.
2. Create a Spec File (Optional):

While not strictly necessary, a spec file allows you to customize the packaging process. You can create a file named main.spec in your project directory with the following content (adjust data path and other options as needed):
```bash
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['.'],
             binaries=[],
             datas=[('path/to/your/data', '.')],
             hiddenimports=[],
             hookspath=[],
             runtimehooks=[],
             excludes=[],
             winnoexcludes=[],
             winextractors=[]
             )
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='your_application_name',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='your_icon.ico'
          )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               runtime_tmpdir=None
               )
```

Replace `path/to/your/data` with the actual path to any data files your application needs.
Adjust your_application_name to your desired executable name.
Optionally, include an icon='your_icon.ico' line to specify an icon for your executable (replace with the path to your icon file).

3. Building the Executable:

Navigate to your project directory in the terminal.

If you created a spec file, run pyinstaller --onefile --specpath . main.spec.

If you don't use a spec file, run pyinstaller --onefile main.py.

The --onefile flag creates a single executable file.
Replace main.py with your actual script name if it's different.
This will build an executable file (usually named your_application_name.exe on Windows or your_application_name on macOS/Linux) in the dist folder within your project directory.

4. Additional Considerations:

Typer Dependencies: Ensure all dependencies required by your Typer application (e.g., click) are installed before building the executable. PyInstaller typically handles most common dependencies, but you might need to explicitly specify them in the spec file if necessary.
Data Files: If your application relies on external data files, make sure to include them in the datas section of the spec file or add them to a directory within the dist folder after building the executable.
Virtual Environments: It's recommended to develop your application in a virtual environment to isolate dependencies. You can activate the virtual environment before building the executable.
By following these steps, you can create a standalone executable for your Typer application using PyInstaller, allowing users to run it without needing Python or additional dependencies installed on their machines.