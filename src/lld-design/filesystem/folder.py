from entry import Entry, validate_name


class Folder(Entry):
    def __init__(self, name: str):
        # Folder("/") represents the root and bypasses name validation.
        # Folder("docs") validates its name and starts with an empty child map.
        if name != "/":
            validate_name(name)
        super().__init__(name)
        self._children: dict[str, Entry] = {}

    def is_directory(self) -> bool:
        # Folder("docs").is_directory() returns True even when it is empty.
        return True

    def get_child(self, name: str) -> Entry:
        # With "docs" directly under root, root.get_child("docs") returns it.
        # A missing name raises FileNotFoundError.
        if name not in self._children:
            raise FileNotFoundError(name)
        return self._children[name]

    def has_child(self, name: str) -> bool:
        # With "docs" directly under root, root.has_child("docs") returns True.
        # A folder nested inside "docs" is checked on docs itself.
        return name in self._children

    def children(self) -> list[Entry]:
        # If root contains only docs, root.children() returns a new list [docs].
        # Changing the list leaves the folder's child map unchanged.
        return list(self._children.values())

    def _add(self, entry: Entry) -> None:
        # root._add(docs) stores docs by name and sets its parent to root.
        # A duplicate name raises FileExistsError.
        validate_name(entry.name)
        if self.has_child(entry.name):
            raise FileExistsError(entry.name)

        # Detach an already attached entry before adding it to another folder.
        if entry.parent is not None:
            raise ValueError("Entry must be detached before attaching")
        self._children[entry.name] = entry
        entry._parent = self

    def _remove(self, name: str) -> Entry:
        # If root contains docs, root._remove("docs") returns it with parent set to None.
        # Removing a missing child raises FileNotFoundError through get_child().
        entry = self.get_child(name)
        del self._children[name]
        entry._parent = None
        return entry
