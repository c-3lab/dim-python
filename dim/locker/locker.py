#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from typing_extensions import Self
from dim.locker._dim_json import _DimJson


class Locker(object):
    """Class to parse dim.json and write dim-lock.json file.

    Args:
        directory: directory which has dim.json to parse
        create_if_missing (optional): True (create {directory}/dim.json if not exist) or False (default)

    Raises:
        FileNotFoundError: {errors} is not "raise" and {directory}/dim.json does not exist
    """

    def __init__(self, directory: str, create_if_missing: bool = False) -> None:
        self._dim_json_path = Path(directory) / "dim.json"
        if self._dim_json_path.exists():
            self._read_dim_json()
        elif create_if_missing:
            self._write_empty_dim_json()
        else:
            raise FileNotFoundError(f"dim.json not found in {directory=}")

    def __eq__(self, other: Self) -> bool:
        return self.defined == other.defined

    @property
    def defined(self) -> dict[str, Any]:
        """Parameter values defined by dim.json file.
        """
        return self._dim_json.to_dict()

    def _read_dim_json(self) -> None:
        """Read {directory}/dim.json file.
        """
        self._dim_json_path.parent.mkdir(exist_ok=True)
        with self._dim_json_path.open("r") as fh:
            content = json.load(fh)
        self._dim_json = _DimJson.from_dict(content)

    def _write_empty_dim_json(self) -> None:
        """Write empty {directory}/dim.json file.
        """
        self._dim_json = _DimJson()
        with self._dim_json_path.open("w") as fh:
            json.dump(self._dim_json.to_dict(), fh, indent=4)

    def run(self) -> Self:
        """Run locking and write dim-lock.json.

        Raises:
            NotImplementedError: implemented later
        """
        raise NotImplementedError
