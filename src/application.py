import argparse
import os
from .tree import Trie

def build_trie(path: str):
    trie = Trie()
    if os.path.exists(path):
        added = trie.load_from_file(path)
        print(f"[INFO] Loaded {added} words from {path}")
    else:
        print("[WARN] Word list not found. Starting empty.")
    return trie

def print_help():
    print("""
Commands:
 prefix <text> [limit]
 search <word>
 add <word>
 delete <word>
 stats
 help
 quit / exit
""")

def repl(trie: Trie):
    print("Type 'help' for commands.")
    while True:
        line = input("autocomplete> ").strip()
        if not line:
            continue

        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd in ("quit", "exit"):
            print("Goodbye!")
            break

        if cmd == "help":
            print_help()

        elif cmd == "prefix":
            if len(args) == 0:
                print("Usage: prefix <text> [limit]")
                continue

            prefix = args[0]
            limit = int(args[1]) if len(args) > 1 else None

            results = trie.get_words_with_prefix(prefix, limit)
            print("\n".join(results) if results else "No matches.")

        elif cmd == "search":
            if len(args) == 0:
                print("Usage: search <word>")
                continue
            print("Found!" if trie.search(args[0]) else "Not found.")

        elif cmd == "add":
            trie.insert(args[0])
            print("Word added.")

        elif cmd == "delete":
            print("Deleted." if trie.delete(args[0]) else "Not found.")

        elif cmd == "stats":
            print(f"Total words stored: {len(trie)}")

        else:
            print("Unknown command. Type 'help'.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/words.txt")
    args = parser.parse_args()

    trie = build_trie(args.data)
    repl(trie)

if __name__ == "__main__":
    main()
