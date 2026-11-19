import unittest

from file_system import FileSystem


class FileSystemTests(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_create_lookup_and_list(self):
        root = self.fs.get("/")
        self.assertEqual(self.fs.list_entries("/"), [])
        docs = self.fs.create_folder("/docs")
        work = self.fs.create_folder("/docs/work")
        notes = self.fs.create_file("/docs/work/notes.txt")
        self.assertIs(docs.parent, root)
        self.assertIs(self.fs.get("/docs/work/notes.txt"), notes)
        self.assertEqual(self.fs.list_entries("/docs"), [work])
        self.assertEqual(self.fs.list_entries("/docs/work"), [notes])
        self.assertEqual(self.fs.read_file("/docs/work/notes.txt"), "")

    def test_read_and_overwrite(self):
        self.fs.create_file("/notes.txt", "first draft")
        self.assertEqual(self.fs.read_file("/notes.txt"), "first draft")
        self.fs.write_file("/notes.txt", "final")
        self.assertEqual(self.fs.read_file("/notes.txt"), "final")

    def test_rename_and_move_preserve_entry_and_content(self):
        self.fs.create_folder("/archive")
        notes = self.fs.create_file("/notes.txt", "hello")
        self.fs.rename("/notes.txt", "draft.txt")
        self.assertIs(self.fs.get("/draft.txt"), notes)
        with self.assertRaises(FileNotFoundError):
            self.fs.get("/notes.txt")

        self.fs.move("/draft.txt", "/archive/final.txt")
        with self.assertRaises(FileNotFoundError):
            self.fs.get("/draft.txt")
        self.assertIs(self.fs.get("/archive/final.txt"), notes)
        self.assertEqual(self.fs.read_file("/archive/final.txt"), "hello")

    def test_delete_nonempty_folder(self):
        docs = self.fs.create_folder("/docs")
        self.fs.create_file("/docs/notes.txt")
        self.fs.delete("/docs")
        self.assertIsNone(docs.parent)
        self.assertEqual(self.fs.list_entries("/"), [])
        with self.assertRaises(FileNotFoundError):
            self.fs.get("/docs/notes.txt")

    def test_invalid_paths(self):
        for path in ("", "docs", "/docs/", "//docs", "/.", "/..", "/bad\x00name", None):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.fs.get(path)

    def test_missing_entries_and_duplicate_names(self):
        with self.assertRaises(FileNotFoundError):
            self.fs.create_file("/missing/notes.txt")
        with self.assertRaises(FileNotFoundError):
            self.fs.delete("/missing")
        docs = self.fs.create_folder("/docs")
        with self.assertRaises(FileExistsError):
            self.fs.create_file("/docs")
        self.assertIs(self.fs.get("/docs"), docs)

    def test_file_and_directory_type_errors(self):
        self.fs.create_file("/notes.txt")
        with self.assertRaises(NotADirectoryError):
            self.fs.get("/notes.txt/child")
        with self.assertRaises(NotADirectoryError):
            self.fs.create_folder("/notes.txt/child")
        with self.assertRaises(NotADirectoryError):
            self.fs.list_entries("/notes.txt")
        with self.assertRaises(IsADirectoryError):
            self.fs.read_file("/")
        with self.assertRaises(IsADirectoryError):
            self.fs.write_file("/", "text")

    def test_non_string_content(self):
        with self.assertRaises(TypeError):
            self.fs.create_file("/notes.txt", 123)
        self.fs.create_file("/notes.txt", "original")
        with self.assertRaises(TypeError):
            self.fs.write_file("/notes.txt", None)
        self.assertEqual(self.fs.read_file("/notes.txt"), "original")

    def test_root_mutations_are_rejected(self):
        self.fs.create_file("/notes.txt")
        for operation, args in (
            (self.fs.create_folder, ("/",)),
            (self.fs.create_file, ("/",)),
            (self.fs.delete, ("/",)),
            (self.fs.rename, ("/", "root")),
            (self.fs.move, ("/", "/new")),
            (self.fs.move, ("/notes.txt", "/")),
        ):
            with self.subTest(operation=operation.__name__, args=args):
                with self.assertRaises(ValueError):
                    operation(*args)

    def test_rejected_rename_and_move_preserve_entries(self):
        source = self.fs.create_file("/source.txt")
        destination = self.fs.create_file("/destination.txt")
        with self.assertRaises(FileExistsError):
            self.fs.rename("/source.txt", "destination.txt")
        self.assertIs(self.fs.get("/source.txt"), source)
        self.assertIs(self.fs.get("/destination.txt"), destination)
        with self.assertRaises(FileExistsError):
            self.fs.move("/source.txt", "/destination.txt")
        self.assertIs(self.fs.get("/source.txt"), source)
        self.assertIs(self.fs.get("/destination.txt"), destination)

    def test_move_into_own_subtree_is_rejected(self):
        docs = self.fs.create_folder("/docs")
        archive = self.fs.create_folder("/docs/archive")
        with self.assertRaises(ValueError):
            self.fs.move("/docs", "/docs/archive/docs")
        self.assertIs(self.fs.get("/docs"), docs)
        self.assertIs(self.fs.get("/docs/archive"), archive)
