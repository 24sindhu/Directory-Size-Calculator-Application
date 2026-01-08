# CLI entry point for Directory Size Calculator
from data.seed_data import build_sample_filesystem
from src.commands import ls, cd, size

def main():
    root = build_sample_filesystem()
    current = root

    print("Welcome to my Directory Explorer!")
    print("Try commands: ls, cd <folder>, cd .., size, exit")

    while True:
        cmd_input = input(f"{current.get_name()}> ").strip().split()

        if not cmd_input:
            continue

        cmd = cmd_input[0]

        if cmd == "ls":
            ls(current)
        elif cmd == "cd" and len(cmd_input) == 2:
            current = cd(current, cmd_input[1])
        elif cmd == "size":
            size(current)
        elif cmd == "exit":
            print("Exiting!")
            break
        else:
            print("Hmm, I didn't get that. Try again!")

if __name__ == "__main__":
    main()