from src.filesystem import File, Directory

def build_sample_filesystem():
    root = Directory("root")

    docs = Directory("docs", parent=root)
    root.add_subdirectory(docs)

    images = Directory("images", parent=root)
    root.add_subdirectory(images)

    docs.add_file(File("resume.pdf", 120))
    docs.add_file(File("notes.txt", 80))

    images.add_file(File("photo1.png", 200))
    images.add_file(File("photo2.png", 300))

    projects = Directory("projects", parent=docs)
    docs.add_subdirectory(projects)
    projects.add_file(File("project1.zip", 400))

    return root