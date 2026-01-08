# to handle commands for Directory Size Calculator CLI
def ls(current):
    """List folders and files in the current directory."""
    if current.subdirectories:
        print(">> Folders in this directory:")
        for name, subdir in current.subdirectories.items():
            print(f" - {subdir.get_name()}/")
    else:
        print("No subfolders here")

    if current.files:
        print(">> Files in this directory:")
        for f in current.files:
            print(f" - {f.get_name()} [{f.get_size()}KB]")
    else:
        print("No files found.")

def cd(current, target):
    """Change directory. Supports '..' to go up."""
    if target == "..":
        if current.parent:
            return current.parent
        else:
            print("you're at root already")
            return current

    if target in current.subdirectories:
        return current.subdirectories[target]

    print(f"folder '{target}' not found")
    return current

def size(current):
    """Print total size of current folder using polymorphic get_size()"""
    total = current.get_size()  # Polymorphic call
    print(f"Total size: {total}KB")