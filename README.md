# dim-python

`dim-python` is a Python implementation of dim (Data Installation Manager): Manage open data in your projects, like a package manager.

## Join community

We are looking for members to develop together as an open source community.

[Slack](https://join.slack.com/t/c3lab-hq/shared_invite/zt-v6zz66n9-1VYkVXC4zoQViWSMdzMTLg)

## Quick Start

### Install the dim

Clone this repository with `git clone` command.

```Bash
git clone https://github.com/c-3lab/dim-python.git
```

Install Python 3.8+.

Then, install `poetry` 1.2.0+ as follows.

Windows:

```Bash
# Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -
# Windows (Powershell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Install dependencies with `poetry`.

```Bash
poetry install
```

### Check version of dim

```Python
import dim
dim.__version__
```

## License

Refer to [MIT License](https://github.com/c-3lab/dim-python/blob/main/LICENSE).
