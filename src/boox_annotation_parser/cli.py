"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mboox_annotation_parser` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``boox_annotation_parser.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``boox_annotation_parser.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import argparse
import sys

from . import serializers, parser

SERIALIZERS = {
    "json": serializers.JsonSerializer,
    "nljson": serializers.NLJsonSerializer,
    "yaml": serializers.YamlSerializer,
}


def main(argv=sys.argv):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-i",
        "--input",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="File to read from (default: stdin)",
    )
    arg_parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="File to write to (default: stdout)",
    )
    arg_parser.add_argument(
        "-f",
        "--format",
        default="yaml",
        choices=SERIALIZERS.keys(),
        help="Format to write output in.",
    )
    args = arg_parser.parse_args(argv[1:])

    serializer = SERIALIZERS[args.format]()
    annotations = parser.get_annotations(args.input)

    args.output.write(serializer.serialize(annotations))
