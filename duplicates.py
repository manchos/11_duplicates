import os
from collections import Counter


def are_files_duplicates(dir_path1, dir_path_2):
    search_dublicates(search_dublicates(dir_path1)+search_dublicates(dir_path_2))


def search_dublicates(path):
    path_f = []
    for dir_path, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            path_f.append((file_name, file_size))
    return [pair[0] for pair in Counter(path_f).most_common() if pair[1] > 1]


if __name__ == '__main__':
    filepath = input('Enter the real path to json file with list of bars:')
    print(search_dublicates(filepath))
