# https://codechalleng.es/bites/161/

import os


def count_dirs_and_files(directory="."):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    file_count = 0
    dir_count = -1

    def recursive_walk(dir, dir_count, file_count):
        for root, dirs, files in os.walk(dir):
            if dirs:
                for dir in dirs:
                    recursive_walk(dir, dir_count, file_count)
            dir_count += 1
            for file in files:
                file_count += 1
        return dir_count, file_count

    return recursive_walk(directory, dir_count, file_count)
