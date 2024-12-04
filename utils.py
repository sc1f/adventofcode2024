def open_input(file_path, callback):
    with open(file_path, "r") as f:
        callback(f)