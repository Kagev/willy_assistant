
from project_willy.methods.imports import os, Path

from project_willy.methods.imports import pickle, json, csv

class FileOperations:

    AUTOSAVE_PATH = Path(os.getcwd()) / 'willy_autosave.bin'

# TXT
    def export_to_txt(file_path, some_dict: dict) -> None:
        result = ''
        with open(file_path, 'w') as fh:
            for k, v in some_dict.items():
                result += f'{k}: {v}\n'
            fh.write(result)

# PICKLE
    def export_to_pickle(file_path, some_data) -> None:
        with open(file_path, "wb") as fh:
            pickle.dump(some_data, fh)

    def autosave_to_pickle(file_path, *args) -> None:
        with open(file_path, "wb") as fh:
            pickle.dump(args, fh)

    def import_from_pickle(file_path):
        with open(file_path, "rb") as fh:
            result = pickle.load(fh)
        return result

# JSON
    def export_to_json(file_path, some_data) -> None:
        with open(file_path, "w") as fh:
            json.dump(some_data, fh)

# CSV
    def export_to_csv(file_path, some_list: list) -> None:
        with open(file_path, 'w', newline='') as fh:
            record_writer = csv.writer(fh)
            for row in some_list:
                record_writer.writerow(row)
