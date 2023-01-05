# dim-python

[![PyPI version](https://badge.fury.io/py/dim-python.svg)](https://badge.fury.io/py/dim-python)
[![Downloads](https://static.pepy.tech/badge/dim-python)](https://pepy.tech/project/dim-python)



`dim-python` is a Python implementation of [dim (Data Installation Manager): Manage open data in your projects, like a package manager](https://github.com/c-3lab/dim).

## Join community

We are looking for members to develop together as an open source community.

[Slack](https://join.slack.com/t/c3lab-hq/shared_invite/zt-v6zz66n9-1VYkVXC4zoQViWSMdzMTLg)

## Quick Start

1. Install the dim

https://github.com/c-3lab/dim#install-the-dim

2. Install the python-dim

```
$ pip install python-dim
```

3. Initialize the project for dim

```
$ dim init
```

Also can initialize the project using dim-python.

4. Use the python-dim

```python
import dim

dim.install('https://example.com/xxx.json', 'example_name', ['encode utf-8'])

print(dim.list())

print(dim.load_data('example_name', 'json'))

```

## Method

* [load_data](#load_data)
* [fetch_data](#fetch_data)
* [load_dim_json](#load_dim_json)
* [load_dim_lock_json](#load_dim_lock_json)
* [init](#init)
* [install](#install)
* [uninstall](#uninstall)
* [update](#update)
* [list](#list)
* [search](#search)

### load_data

```python
dim.load_data('name', 'csv')
```

#### Parameters

* name(requrire)
  * Specify data name
* file_type(option)
  * Specify 'text' or 'json' or 'csv'
  * default: 'text'
* dim_file_path(option)
  * Specify a file path existing dim.json and dim-lock.json, data_files 
  * default: './'
* encoding(option)
  * Specify encoding of data
  * default: 'utf-8'

#### Return

Return type each file_type
text: str
csv:  csv.DictReader object
json: dict

---

### fetch_data

```python
dim.fetch_data('name')
```

#### Parameters

* name(requrire)
  * Specify data name
* dim_file_path(option)
  * Specify a file path existing dim.json and dim-lock.json, data_files 
  * default: './'

#### Return

requests.Response object

---

### load_dim_json

```python
dim.load_dim_json()
```


#### Parameters

* dim_file_path(option)
  * Specify a file path existing dim.json and dim-lock.json, data_files 
  * default: './'
* encoding(option)
  * Specify encoding of data
  * default: 'utf-8'

#### Return

dict

---

### load_dim_lock_json

```python
dim.load_dim_lock_json()
```

#### Parameters

* dim_file_path(option)
  * Specify a file path existing dim.json and dim-lock.json, data_files 
  * default: './'
* encoding(option)
  * Specify encoding of data
  * default: 'utf-8'

#### Return

dict

---

### init

```python
dim.init()
```

#### Parameters

#### Return

boolean

---

### install

```python
dim.install()
```

#### Parameters

* source(require)
* name(require)
* postprocesses(option)
  * default: []
* from_file(option)
  * default: False
* force(option)
  * default: False
* async_install(option)
  * default: False

#### Return

boolean

---

### uninstall

```python
dim.uninstall()
```

#### Parameters
* name(require)

#### Return

boolean

---

### update

```python
dim.update()
```

#### Parameters

* name(require)
* async_install(option)
  * default: False

#### Return

boolean

---

### list

```python
dim.list()
```

#### Parameters

* simple(option)
  * default: False
  
#### Return

str

---

### search

```python
dim.search()
```

#### Parameters

* keyword(require)
* number(option)
  * default: 10
  
#### Return

str

---

## Build

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
