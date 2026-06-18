import os

def save_uploaded_file(file_name, content):
    """
    Save the uploaded PDF into the project's data/input folder.
    """

    # Project Root Directory
    project_root=os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)   
            )
        )
    )

    # Folder where uploaded PDFs are stored
    upload_dir = os.path.join(
        project_root,
        "data",
        "input"
    )
    # Create folder if it does not exist
    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    # Full file path
    file_path = os.path.join(
        upload_dir,
        file_name
    )
    # Save uploaded file
    with open(file_path, "wb") as file:
        file.write(content)

    return file_path