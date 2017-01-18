import os
import argparse
from collections import defaultdict
from collections import namedtuple

file_info_class = namedtuple('FileInfo', ['name', 'size'])

# data structure :
# {(FileInfo('file1_name','file1_size'):[file1_path_1,file1_path_2],FileInfo('file2_name','file2_size'):[file2_path_1]}


def search_dublicates(path):
    file_dict_by_name_size_path = defaultdict(list)
    for dir_path, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_dict_by_name_size_path[file_info_class(file_name, file_size)].append(file_path)
    return dict(file_info for file_info in file_dict_by_name_size_path.items() if len(file_info[1]) > 1)


def print_duplicates_to_terminal(duplicates):
    for file_info, file_paths in duplicates.items():
        print('\n File: %s found in:' % file_info.name)
        for path in file_paths:
            print(path)


def directory(raw_path):
    if not os.path.isdir(raw_path):
        raise argparse.ArgumentTypeError('"{}" is not an existing directory'.format(raw_path))
    return os.path.abspath(raw_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get duplicated files")
    parser.add_argument("-d", "--dir", type=directory, dest="dir", required=True)
    args = parser.parse_args()
    duplicates_list = search_dublicates(args.dir)
    print('Found {0} duplicates:'.format(len(duplicates_list)))
    print_duplicates_to_terminal(duplicates_list)


