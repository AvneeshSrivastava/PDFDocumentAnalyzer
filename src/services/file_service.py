import os

def save_uploaded_file(file_name, content):

    file_path = os.path.join(
        "data",
        "input",
        file_name
    )

    with open(file_path, "wb") as file:
        file.write(content)

    return file_path