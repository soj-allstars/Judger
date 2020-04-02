import os


def create_file_to_write(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')
