# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import sys, os, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, filename="qwerty_log.log",filemode="w")
if os.path.exists(sys.argv[1]):
    for root, dirs, files in os.walk(sys.argv[1]):
        path = root.split(os.sep)
        path = Path(root)
        p_dir = path.parent.absolute()
        r_dir = os.path.basename(root)
        logging.info(f'{r_dir} \t\t\t\t DIR \t\t\t\t {p_dir}')
        print(f'{r_dir} \t\t\t\t DIR \t\t\t\t {p_dir}')
        for file in files:
            f_name, f_ext = file.split('.')
            logging.info(f'{f_name} \t\t\t\t {f_ext} \t\t\t\t {r_dir}')
            print(f'{f_name} \t\t\t\t {f_ext} \t\t\t\t {r_dir}')