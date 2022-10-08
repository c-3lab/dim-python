#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Dict, Optional
from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin


@dataclass
class _DimJsonContent(DataClassJsonMixin):
    """Dataclass to parse the contents of dim.json file.

    Args:
        name: dataset title
        url (optional): URL to retrieve the dataset
        catalogUrl (optional): URL if dataset is available in CKAN
        catalogResourceId (optional): dataset ID if dataset is available in CKAN
        headers (optional): headers of the dataset

    Note:
        URL of CKAN is https://www.geospatial.jp/ckan/
    """
    name: str
    url: Optional[str] = field(default=None)
    catalogUrl: Optional[str] = field(default=None)
    catalogResourceId: Optional[str] = field(default=None)
    postProcesses: list[str] = field(default_factory=list)
    headers: Dict[str, str] = field(default_factory=dict)


@dataclass
class _DimJson(DataClassJsonMixin):
    """Dataclass to parse dim.json file.

    Args:
        fileVersion: version number of dim.json file structure, fixed to '1.1' at this time.
        contents: list of database definitions
    """
    fileVersion: str = field(init=False)
    contents: list[_DimJsonContent] = field(default_factory=list)

    def __post_init__(self):
        self.fileVersion = "1.1"
