import argparse
import copy
import pathlib


def main():
    parser = argparse.ArgumentParser(
        description="Process TeX files by generating one file with the solution and one without."
    )
    parser.add_argument(
        "infile",
        nargs="?",
        metavar="SRC",
        type=pathlib.Path,
        help="Input TeX file",
    )
    args = parser.parse_args()

    content = args.infile.read_text().splitlines()

    statement = copy.copy(content)
    solution = copy.copy(content)

    print(f"Processing {args.infile}...")

    for i, line in enumerate(content):
        if r"\def\AvecSolutions{}" in line:
            if line.startswith("%"):
                statement[i] = line
                solution[i] = line[1:]
            else:
                statement[i] = "%" + line
                solution[i] = line

            break

    args.infile.write_text("\n".join(statement))
    (args.infile.with_stem(args.infile.stem + "_solution")).write_text("\n".join(solution))


if __name__ == "__main__":
    main()
