from dataclasses import dataclass, field
from collections import defaultdict
from typing import Optional, List

# be sure to update tag_order_list along with this default dict
tag_color_map = defaultdict(lambda: "yellow")
tag_color_map["@overdue"] = "purple"
tag_color_map["@important"] = "red"
tag_color_map["@today"] = "cyan"
tag_color_map["@week"] = "green"
tag_color_map["@month"] = "blue"

# be sure to update tag_color_map default dict along with this list
tag_order_list: List[str] = ["@overdue", "@important", "@today", "@week", "@month"]

@dataclass(kw_only=True)
class Todo:
    id: int
    desc: str
    tag: Optional[str]
    status: str = "in-progress"
    modified: str

    # validation
    def __post_init__(self):
        if self.status not in ['in-progress', 'completed']:
            raise ValueError("invalid status")