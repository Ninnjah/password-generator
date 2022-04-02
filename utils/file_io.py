import re
from pathlib import Path
import string
from typing import Generator, List, Union, NoReturn
import unicodedata


def filename_check(filename: str) -> int:
    """Filename validator

    :returns int: 0 - filename is valid
                  1 - filename length more than char limit
                  2 - filename consist restricted char
    """
    char_limit: int = 255
    valid_chars: str = f"-_.() {string.ascii_letters}{string.digits}"

    if len(filename) > 255:
        return 1

    elif any(x for x in filename if x not in valid_chars):
        return 2

    else:
        return 0


def save_to_file(data: Union[List[str], Generator]) -> NoReturn:
    """Saves data to file

    :param data: Union[List[str], Generator] - list or generator of data

    :return None:
    """
    while True:
        filename = input("Enter file name (default-\"passwords\"): ") or "passwords"
        err = filename_check(filename)

        if not err:
            break

        elif err == 1:
            print("Filename length more than char limit")

        elif err == 2:
            print("Filename consist restricted char")

    save_file: Path = Path(filename)

    # Write data to filename
    with open(save_file.with_suffix(".txt"), "a+", encoding="utf-8") as f:
        f.writelines([x+"\n" for x in data])

