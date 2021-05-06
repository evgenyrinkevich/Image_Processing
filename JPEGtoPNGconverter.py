import sys
import os
from PIL import Image


def convert(source, dest='png'):
    """
    converts jpeg files from source directory to png in dest directory
    """
    dest_path = os.path.join(os.getcwd(), dest)
    os.makedirs(dest_path, exist_ok=True)
    source_path = os.path.join(os.getcwd(), source)
    for file in os.listdir(source_path):
        if os.path.isfile(os.path.join(source_path, file)):
            if file.lower().endswith('jpeg') or file.lower().endswith('jpg'):
                img = Image.open(os.path.join(source_path, file))
                f, e = file.split('.')
                dest_file_name = os.path.join(dest_path, f + '.png')
                img.save(dest_file_name, 'png')


if __name__ == '__main__':
    source_folder = os.getcwd()
    try:
        source_folder = sys.argv[1]
        dest_folder = sys.argv[2]
    except IndexError:
        print(f'1 or 2 paths not given - converting from {source_folder} to png directory')
    try:
        convert(source_folder, dest_folder)
    except NameError:
        convert(source_folder)
