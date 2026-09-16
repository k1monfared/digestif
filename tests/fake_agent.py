"""A fake agent for tests. Copies a canned graph into the working directory."""

import argparse
import shutil
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", required=True, help="canned graph.json to install")
    args = parser.parse_args()
    shutil.copyfile(args.graph, Path.cwd() / "graph.json")
    print("fake agent wrote graph.json")
