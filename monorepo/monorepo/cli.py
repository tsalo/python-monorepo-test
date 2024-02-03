"""Command-line interface for the monorepo package."""

import argparse

from monorepo.workflows import run_workflow


def _get_parser():
    """Parse command line inputs for t2smap.

    Returns
    -------
    parser.parse_args() : argparse dict
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        dest="data",
        nargs="+",
        metavar="FILE",
        type=float,
        help="Space-separated list of floats to process",
        required=True,
    )

    return parser


def main(argv=None):
    """Run the workflow."""
    options = _get_parser().parse_args(argv)
    kwargs = vars(options)
    run_workflow(**kwargs)


if __name__ == "__main__":
    raise Exception("No!")
