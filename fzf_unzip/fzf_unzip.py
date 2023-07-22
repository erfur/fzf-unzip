"""Main module."""

import zipfile
from fzf import fzf_prompt
import os


class FzfUnzip:
    def __init__(self, zip_file_name: str, dry_run: bool) -> None:
        self.zipfile = zip_file_name
        self.dry_run = dry_run
        self.archive = zipfile.ZipFile(self.zipfile, mode="r")

    def list_entries(self):
        return self.archive.namelist()

    def extract_file(self, filename):
        file_basename = os.path.basename(filename)
        if self.dry_run:
            print(f'[*] Extracting {filename} to {os.path.join(os.curdir, os.path.basename(filename))}')
        else:
            with open(os.path.join(os.curdir, file_basename), 'wb') as f:
                f.write(self.archive.read(filename))

    def run(self):
        result = fzf_prompt(self.list_entries())

        if result is None:
            return

        self.extract_file(result)
