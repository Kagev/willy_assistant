import re, os, shutil, time, tarfile, concurrent.futures, logging, argparse
from pathlib import Path
from threading import Thread
from multiprocessing import cpu_count
from typing import Tuple

parse_list = {"documents": [], "video": [], "audio": [], "images": [], "archives": [], None: []}
extentions = {"identified": [], "unidentified": []}

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", required=True, help="Input folder")
parser.add_argument("--output", "-o", default="dist", help="Output folder")

args = vars(parser.parse_args())

source = args.get("source")
output = args.get("output")

folders = []
file_categories = set()


def normalize(file: Path) -> Path:
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a",
        "b",
        "v",
        "g",
        "d",
        "e",
        "e",
        "j",
        "z",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "r",
        "s",
        "t",
        "u",
        "f",
        "h",
        "ts",
        "ch",
        "sh",
        "sch",
        "",
        "y",
        "",
        "e",
        "yu",
        "ya",
        "je",
        "i",
        "ji",
        "g",
    )
    mapping = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        mapping[ord(c)] = l
        mapping[ord(c.upper())] = l.upper()
    edited_file_name = file.name.replace(file.suffix, "")
    edited_file_name = edited_file_name.translate(mapping)
    edited_file_name = re.sub(r"[^a-zA-Z0-9_]", "_", edited_file_name)
    return file.rename(str(file).replace(file.name, f"{edited_file_name}{file.suffix}"))


def identify_file(file: Path) -> Tuple[str, str, str] | Tuple[None, str, str]:
    POSSIBLE_EXTENSIONS = {
        "documents": (".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx", ".ods", ".xlx"),
        "video": (".avi", ".mp4", ".mov", ".mkv"),
        "audio": (".mp3", ".ogg", ".wav", ".amr"),
        "images": (".jpeg", ".png", ".jpg", ".svg"),
        "archives": (".zip", ".gz", ".tar", ".7z"),
    }
    file_extension = file.suffix.lower()
    for name, extensions in POSSIBLE_EXTENSIONS.items():
        if file_extension in extensions:
            return name, file_extension, 'identified'
    return None, file_extension, 'unidentified'


def read_folder(path: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            folders.append(normalize(element))
            read_folder(normalize(element))


def copy_file(folder: Path, folder_name: str) -> None:
    for element in folder.iterdir():
        if element.is_file():
            ext = element.suffix.lower()
            file_category = identify_file(element)
            file_categories.add(file_category[0])
            if file_category[0] is None:
                new_path = output_folder / 'unidentified'
            else:
                new_path = output_folder / file_category[0] / ext[1:]
            new_path.mkdir(exist_ok=True, parents=True)
            shutil.move(element, new_path / element.name)



if __name__ == "__main__":
    log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log")
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logging.basicConfig(
        filename=os.path.join(log_folder, "clean_folder.log"),
        level=logging.ERROR,
        format="%(asctime)s %(levelname)s: %(threadName)s - %(message)s",
    )

    base_folder = Path(source)
    output_folder = Path(output)
    folders.append(base_folder)
    read_folder(base_folder)

    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder, folder.name))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    for category in file_categories:
        category_path = output_folder / category
        category_path.mkdir(exist_ok=True)

    for category in file_categories:
        if category is not None:
            category_path = output_folder / category
            category_path.mkdir(exist_ok=True)

    print("Sorting completed.")
