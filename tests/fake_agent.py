"""A fake agent for tests. Copies canned artifacts into the working directory."""

import argparse
import shutil
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", help="canned graph.json to install")
    parser.add_argument("--prose", help="canned fitsegid.md to install")
    args = parser.parse_args()
    if args.graph:
        shutil.copyfile(args.graph, Path.cwd() / "graph.json")
        print("fake agent wrote graph.json")
    if args.prose:
        shutil.copyfile(args.prose, Path.cwd() / "fitsegid.md")
        print("fake agent wrote fitsegid.md")
