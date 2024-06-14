import os
import os.path
import subprocess

def find_files(root, ext):
    """ Finds all files with a given extension (ext) in a directory (root) and all it's sub-directories
        ext = string; file extension including the dot, e.g. '.mp3'
        root = absolute path of top root directory to start searching
        Returns a list of absolute paths of files as strings
    """
    # For testing purposes I'm skipping these two directories as they have loads of files
    skip_dir = ['__pycache__', 'ThinkPython-master']
    # list to hold search results
    found = []  
    for dirpath, dirnames, filenames in os.walk(root):
        for directory in skip_dir:
            if directory in dirnames:
                dirnames.remove(directory)
        for file in filenames:
            file_ext = os.path.splitext(file)[1]
            if file_ext == ext:
                found.append(os.path.join(dirpath, file))
    return found

def get_hash(path):
    """ Gets an SHA256 hash of the requested file using Powershell's Get-FileHash cmdlet
        path = string; an absolute path of the file
        Returns a string
    """
    command = '$my_hash = Get-FileHash ' + '\'' + path + '\'' +'\n$my_hash.hash'
    ps_output = subprocess.run(['powershell', '-Command', command], capture_output=True)
    sha256 = str(ps_output.stdout, encoding='utf-8').strip()

    return sha256

def find_duplicates(path, ext):
    """ Finds all duplicate files with a given extension (ext) in a directory (path) and all sub-directories
        path = string
        ext = string
        Returns a list of lists of strings (each nested list corresponds to a single grouping of duplicate files sharing the same hash)
    """
    hashes = {}
    
    for file in find_files(path, ext):
        file_hash = get_hash(file)
        hashes[file_hash] = hashes.get(file_hash, []) + [file]
    
    duplicates = []
    for h, files in hashes.items():
        if len(files) > 1:
            duplicates.append(files)
    return duplicates
            
def print_find_duplicates(path, ext):
    count = 1
    for group in find_duplicates(path, ext):
        print('***', count, '***')
        for file in group:
            print(file)
        print('')
        count += 1
    

test_path = os.path.join('D:', os.sep, 'Dropbox', 'General Reference', 'Think Python', 'Chapter 14', 'Test')
print_find_duplicates(test_path, '.txt')

# test_file = 'D:\\Dropbox\\General Reference\\Think Python\\Chapter 13\\words.txt'
# get_hash(test_file)
