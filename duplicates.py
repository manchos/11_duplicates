import os


def search_dublicates(path):
    file_dict_by_name_size_path = {}
    for dir_path, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_name_size = str(file_name) + '_' + str(file_size)
            if file_name_size not in file_dict_by_name_size_path:
                file_dict_by_name_size_path[file_name_size] = [file_path]
            else:
                file_dict_by_name_size_path[file_name_size].append(file_path)
    return [i for i in file_dict_by_name_size_path.items() if len(i[1]) > 1]


def print_duplicates_to_terminal(duplicates):
    for i in duplicates:
        print('\n File: %s found in:' % (i[0].split('_')[0]))
        for dub in i[1]:
            print(dub)


if __name__ == '__main__':
    dir_path = input('Enter the real path to directory:')
    if not os.path.exists(dir_path):
        print('Folder not fount')
        exit()
    duplicates_list = search_dublicates(dir_path)
    print('Found {0} duplicates:'.format(len(duplicates_list)))
    print_duplicates_to_terminal(duplicates_list)

