
# from project_willy.methods.imports import Path, re, os, shutil
import re, os, shutil
from pathlib import Path
from threading import Thread
import logging, argparse
import tarfile


parse_list = {'documents': [], 'video': [], 'audio': [], 'images': [], 'archives': [], None: []}
extentions = {'identified': [], 'unidentified': []}

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", required=True, help="Input folder")
parser.add_argument("--output", "-o", default="dist", help="Output folder")

args = vars(parser.parse_args())

source = args.get("source")
output = args.get("output")

folders = []
file_categories = set()

def parse_files(path: Path) -> None:
    global parse_list
    global extentions
    DIRECTORIES = ('documents', 'video', 'audio', 'images', 'archives')
    for file in path.iterdir():
        if file.is_file():
            name, file_extension, status = identify_file(file)
            parse_list[name].append(file.name)
            extentions[status].append(file_extension)
        elif file.is_dir():
            if file.name.lower() in DIRECTORIES:
                continue
            elif not os.listdir(file):
                os.rmdir(file)
                continue
            else:
                parse_files(normilize(file))


def identify_file(file: Path) -> tuple:
    POSSIBLE_EXTENTIONS = {
        'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.xls', '.ods' '.pptx'),
        'video': ('.avi', '.mp4', '.mov', '.mkv'),
        'audio': ('.mp3', '.ogg', '.wav', '.amr'),
        'images': ('.jpeg', '.png', '.jpg', '.svg'),
        'archives': ('.zip', '.gz', '.tar', '.7z', '.xz')
    }
    file_extension = file.suffix.lower()
    for name, extensions in POSSIBLE_EXTENTIONS.items():
        for extension in extensions:
            if file_extension == extension:
                move_to_directory(normilize(file), name)
                return name, file_extension, 'identified'
    return None, file_extension, 'unidentified'


def normilize(file: Path) -> Path:
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s",
        "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
    )
    map = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        map[ord(c)] = l
        map[ord(c.upper())] = l.upper()
    edited_file_name = file.name.replace(file.suffix, '')
    edited_file_name = edited_file_name.translate(map)
    edited_file_name = re.sub(r'[^a-zA-Z0-9_]', '_', edited_file_name)
    return file.rename(str(file).replace(file.name, f'{edited_file_name}{file.suffix}'))


import tarfile

def move_to_directory(file: Path, directory_name: str) -> None:
    directory_path = Path(str(file).replace(file.name, directory_name))
    archive_path = directory_path / file.name.replace(file.suffix, '')
    try:
        os.mkdir(directory_path)
        if file.suffix in ('.zip', '.gz', '.tar', '.7z', '.xz'):
            os.mkdir(archive_path)
    except FileExistsError:
        None
    finally:
        if file.suffix == '.zip':
            shutil.unpack_archive(file, archive_path)
        elif file.suffix == '.gz':
            with tarfile.open(file, 'r:gz') as tar:
                tar.extractall(archive_path)
        elif file.suffix == '.tar':
            with tarfile.open(file, 'r') as tar:
                tar.extractall(archive_path)
        elif file.suffix == '.7z':
            with tarfile.open(file, 'r') as sz:
                sz.extractall(archive_path)
        else:
            shutil.move(file, directory_path)


def launch_script(path: Path) -> None:
    for element in path.iterdir():
        try:
            if element.is_dir():
                parse_files(path)
                print(f'\n| IDENTIFIED: {set(extentions["identified"])} |')
                print(f'| UNIDENTIFIED: {set(extentions["unidentified"])} |')
                print('\n{:^40}\n'.format('---SUCCESSFULL---'))
                folders.append(element)
                launch_script(element)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")


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
    launch_script(base_folder)

    threads = []
    for folder in folders:
        th = Thread(target=move_to_directory, args=(folder, folder.name))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    # for category in file_categories:
    #     category_path = output_folder / category
    #     category_path.mkdir(exist_ok=True)

    print("Mission complet")