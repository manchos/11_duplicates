import os
from collections import defaultdict
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'size'])

# data structure :
# {(FileInfo('file1_name','file1_size'):[file1_path_1,file1_path_2],FileInfo('file2_name','file2_size'):[file2_path_1]}


def search_dublicates(path):
    file_dict_by_name_size_path = defaultdict(list)
    for dir_path, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_name_size_key = str(file_name) + '/' + str(file_size)
            if file_name_size_key not in file_dict_by_name_size_path:
                file_dict_by_name_size_path[file_name_size_key] = [file_path]
                d[(file.name, file.size)].append(path)
            else:
                file_dict_by_name_size_path[file_name_size_key].append(file_path)
    return [file_info for file_info in file_dict_by_name_size_path.items() if len(file_info[1]) > 1]


def print_duplicates_to_terminal(duplicates):
    for file_info in duplicates:
        file_name = file_info[0].split('/')[0]
        print('\n File: %s found in:' % file_name)
        for file_path in file_info[1]:
            print(file_path)


if __name__ == '__main__':
    dir_path = input('Enter the real path to directory name: ')
    if not os.path.exists(dir_path):
        print('Folder not fount')
        exit()
    duplicates_list = search_dublicates(dir_path)
    print('Found {0} duplicates:'.format(len(duplicates_list)))
    print_duplicates_to_terminal(duplicates_list)

