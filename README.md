# Jotdown Python

A Python version of Jotdown. Final distributable executable file is `11.2 mb` huge !!!


## Creating a Python executable

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