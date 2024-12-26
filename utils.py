def solve(file_path, callback):
    with open(file_path, "r") as f:
        callback(f)