class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.subdirectories = {}
        self.files = []

    def add_file(self, file: File):
        self.files.append(file)

    def add_directory(self, directory):
        self.subdirectories[directory.name] = directory

    def get_size(self) -> int:
        total = sum(file.size for file in self.files)
        for subdir in self.subdirectories.values():
            total += subdir.get_size()
        return total