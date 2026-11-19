from entry import validate_name, Entry
from file import File
from folder import Folder


class FileSystem:
    def __init__(self):
        # Each filesystem starts with an empty root at "/".
        self._root = Folder("/")

    @staticmethod
    def _parts(path: str) -> list[str]:
        # Split "/docs/notes.txt" into ["docs", "notes.txt"]. The root has no parts.
        if not isinstance(path, str) or not path.startswith("/"):
            raise ValueError("Path must be absolute")

        if path == "/":
            return []

        parts = path[1:].split("/")

        for part in parts:
            validate_name(part)
        return parts

    def _walk(self, parts: list[str]) -> Entry:
        # Follow ["docs", "notes.txt"] from the root, one child at a time.
        current = self._root
        for part in parts:
            if not isinstance(current, Folder):
                raise NotADirectoryError(current.name)
            current = current.get_child(part)
        return current

    def _parent_and_name(self, path: str) -> tuple[Folder, str]:
        # For "/docs/notes.txt", return the docs folder and the name "notes.txt".
        parts = self._parts(path)
        if not parts:
            raise ValueError("Operation is not allowed on root")

        parent = self._walk(parts[:-1])
        if not isinstance(parent, Folder):
            raise NotADirectoryError(parent.name)

        return parent, parts[-1]

    def get(self,path:str)->Entry:
        # get("/docs/notes.txt") returns the entry stored at that path.
        return self._walk(self._parts(path))

    def create_folder(self, path: str) -> Folder:
        # create_folder("/docs/work") adds work under the existing docs folder.
        parent, name = self._parent_and_name(path)
        folder = Folder(name)
        parent._add(folder)
        return folder

    def create_file(self, path: str, content: str = "") -> File:
        # create_file("/docs/notes.txt", "hello") stores a file with initial content.
        parent, name = self._parent_and_name(path)
        file = File(name, content)
        parent._add(file)
        return file

    def list_entries(self, path: str) -> list[Entry]:
        # list_entries("/docs") returns only the entries directly inside docs.
        folder = self.get(path)
        if not isinstance(folder, Folder):
            raise NotADirectoryError(path)
        return folder.children()

    def read_file(self, path: str) -> str:
        # read_file("/docs/notes.txt") returns the stored text, such as "hello".
        entry = self.get(path)
        if not isinstance(entry, File):
            raise IsADirectoryError(path)
        return entry.content

    def write_file(self, path: str, content: str) -> None:
        # write_file("/docs/notes.txt", "updated") replaces the entire contents.
        if not isinstance(content, str):
            raise TypeError("Content must be a string")
        entry = self.get(path)
        if not isinstance(entry, File):
            raise IsADirectoryError(path)
        entry.content = content

    def delete(self, path: str) -> None:
        # delete("/docs") detaches docs together with any entries inside it.
        parent, name = self._parent_and_name(path)
        parent._remove(name)  # Nonempty folders are detached as a subtree.

    def rename(self, path: str, new_name: str) -> None:
        # rename("/docs/notes.txt", "draft.txt") keeps the file inside docs.
        validate_name(new_name)
        parent, old_name = self._parent_and_name(path)
        entry = parent.get_child(old_name)
        if parent.has_child(new_name):
            raise FileExistsError(new_name)
        parent._remove(old_name)
        entry._name = new_name
        parent._add(entry)

    def move(self, source: str, destination: str) -> None:
        # move("/docs/notes.txt", "/archive/notes.txt") takes a full destination path.
        source_parent, source_name = self._parent_and_name(source)
        entry = source_parent.get_child(source_name)
        destination_parent, destination_name = self._parent_and_name(destination)

        # Walking upward catches cycles such as moving /docs to /docs/archive/docs.
        current = destination_parent
        while current is not None:
            if current is entry:
                raise ValueError("Cannot move a folder into its own subtree")
            current = current.parent
        if destination_parent.has_child(destination_name):
            raise FileExistsError(destination)

        # All expected validation failures happen before the first mutation.
        source_parent._remove(source_name)
        entry._name = destination_name
        destination_parent._add(entry)

