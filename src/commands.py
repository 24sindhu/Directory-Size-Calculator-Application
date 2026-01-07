# to handle basic commands: ls, cd, size
def ls(current):
    """List folders and files in the current directory."""
    if current.subdirectories:
        print(">> Folders in this directory:")
        for name in current.subdirectories:
            print(f" - {name}/")
    else:
        print("No subfolders here!")

    if current.files:
        print(">> Files in this directory:")
        for f in current.files:
            print(f" - {f.name} [{f.size}KB]")
    else:
        print("No files found. You can add some!")

def cd(current, target):
    """Change directory. Supports going up with '..'."""
    if target == "..":
        if current.parent:
            return current.parent
        else:
            print("Already at root.")
            return current

    if target in current.subdirectories:
        return current.subdirectories[target]

    print(f"folder '{target}' not found")
    return current

def size(current):
    """Print the total size of current directory including subdirectories."""
    total = current.get_size()
    print(f"Total size: {total}KB")