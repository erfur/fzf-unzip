"""Console script for fzf_unzip."""
import sys
import click

from fzf_unzip.fzf_unzip import FzfUnzip


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("--dry-run", is_flag=True)
def main(filename, dry_run):
    FzfUnzip(filename, dry_run).run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
