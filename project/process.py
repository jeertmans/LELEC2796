import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Process Jupyter notebook by removing lines between two patterns."
    )
    parser.add_argument(
        "infile",
        nargs="?",
        metavar="SRC",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input file",
    )
    parser.add_argument(
        "outfile",
        nargs="?",
        metavar="DEST",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="Output file",
    )
    parser.add_argument(
        "--between",
        nargs="?",
        dest="start",
        metavar="START",
        type=str,
        default=":START-REMOVE:",
        help="pattern indicating start of lines removal",
    )
    parser.add_argument(
        "--and",
        nargs="?",
        dest="end",
        metavar="END",
        type=str,
        default=":END-REMOVE:",
        help="pattern indicating end of lines removal",
    )
    args = parser.parse_args()
    notebook = json.load(args.infile)
    for c, cell in enumerate(notebook.get("cells", [])):
        lines = cell.setdefault("source", [])
        i = 0
        while i < len(lines):
            if args.start in lines[i]:
                j = i + 1
                while j < len(lines):
                    if args.end in lines[j]:
                        del lines[i : j + 1]
                        break
                    j += 1

                if j == len(lines):
                    raise ValueError(
                        f"Could not find ending for pattern starting on cell {c}, "
                        f"line {i}:\n\t{lines[i]}"
                    )
            i += 1

    json.dump(notebook, args.outfile, indent=1)


if __name__ == "__main__":
    main()
