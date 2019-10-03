#!/usr/bin/env python3
# by rog

"""

Change the delimination of the file

"""

import argparse
import csv


def main():
    args = get_args()
    inputfile = args.inputfile
    outputfile = args.outputfile
    indelimiter = args.indelimiter
    inquote = args.inquote

    csv.register_dialect("indelimiter", delimiter=indelimiter)

    lines = []
    with open(inputfile, mode="rt") as file_to_fix:
        reader = csv.reader(file_to_fix, dialect="indelimiter", quoting=csv.QUOTE_NONE, quotechar=inquote)
        for row in reader:
            lines.append(row)

    with open(outputfile, mode="wt") as fixed_file:
        writer = csv.writer(fixed_file)
        for row in lines:
            writer.writerow(row)


def get_args():
    """
    Supports the command line arguments below
    Returns:
        args
    """

    parser = argparse.ArgumentParser(
        description="Change delimiter of input file to specified delimiter"
    )
    parser.add_argument(help="input file", type=str, dest="inputfile")
    parser.add_argument(help="output file", type=str, dest="outputfile")
    parser.add_argument(
        "--in-delimiter",
        help="input delimiter",
        type=str,
        dest="indelimiter",
        default="|",
    )
    parser.add_argument(
        "--in-quote", help="input quote", type=str, dest="inquote", default="'"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
