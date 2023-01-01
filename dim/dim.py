import os


DIM_FILE_PATH = os.environ.get('DIM_FILE_PATH', './')


def load(name, file_type='text', dim_lock_path=DIM_FILE_PATH):
    pass


def install(source, name, postprocesses=[], force=False, async_install=False):
    pass


def uninstall(name):
    pass


def update(name, async_insatll=False):
    pass


def list():
    pass


def search(keyword, number=10):
    pass
