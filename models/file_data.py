from dataclasses import dataclass, field
from typing import List
from models.todo import Todo


@dataclass(kw_only=True)
class FileData:
    todos:  List[Todo]