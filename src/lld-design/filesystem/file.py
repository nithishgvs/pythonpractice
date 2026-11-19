from entry import Entry, validate_name


class File(Entry):
    def __init__(self, name: str, content: str = " "):
        validate_name(name)
        if not isinstance(content, str):
            raise TypeError("Content must be string")
        super().__init__(name)
        self.content = content

    def is_directory(self) -> bool:
        return False
