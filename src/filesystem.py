from abc import ABC, abstractmethod

# Abstract base class for both File and Directory
class FileSystemItem(ABC):
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

class File(FileSystemItem):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

class Directory(FileSystemItem):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = [] 
        self.subdirectories = {} 

    def add_file(self, file):
        self.files.append(file)

    def add_subdirectory(self, directory):
        self.subdirectories[directory.name] = directory

    def get_size(self):
    #call get_size on all contained items
        total = 0
        for f in self.files:
            total += f.get_size()  
        for sub in self.subdirectories.values():
            total += sub.get_size() 
        return total

    def get_name(self):
        return self.name