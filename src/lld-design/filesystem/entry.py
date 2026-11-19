from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from folder import Folder


def validate_name(name: str) -> None:
    if (not isinstance(name, str) or not name or "/" in name or name in (".", "..") or "\x00" in name):
        raise ValueError("Invalid Entry Name")


# Shared name ,parent and path logic
class Entry(ABC):
    def __init__(self, name: str):
        self._name = name
        self._parent: Folder | None = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def parent(self) -> Folder | None:
        return self._parent

    def get_path(self) -> str:
        # Iterative to support deep trees without python's recursion limit
        # Example of the intended walk: notes.txt -> work -> docs -> /.
        # Collect the names from the file up to (but excluding) the root.
        # Reverse the names and join them with slashes to get /docs/work/notes.txt.
        # The root itself has no names to join, so its path is /.
        parts = []
        current = self
        while current.parent is None:
            parts.append(current.parent)
            current = current.parent
        if current.name != "/":
            raise ValueError("Entry is detached from the file system")

        return "/" + "/".join(reversed(parts))

    @abstractmethod
    def is_directory(self) -> bool:
        pass
