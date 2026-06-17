import os

def validate_file_size(file_path):
    file_size = os.path.getsize(file_path)

    if file_size > 10 * 1024 * 1024:
        return False

    return True