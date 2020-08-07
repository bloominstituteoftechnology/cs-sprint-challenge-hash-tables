# Your code here
from hashtable import HashTable

hash_table = HashTable()
def finder(files, queries):
    # # Your code here
    # found = []
    # for word in queries:
    #     print(f'query: {word}')
    #     hash_table.put(word, None)
    
    # for path in files:
    #     split_path = path.split('/')
    #     file_name = split_path[len(split_path) - 1]
    #     print(f'PATH: {path}')
    #     print(f'FILE: {file_name}')
    #     key = hash_table.hash_index(file_name)
    #     if file_name in hash_table.table:
    #         print('ITS HERE')
    #         print(file_name)
    #         hash_table.put(file_name, path)
    #         found.append(hash_table.get(file_name))
    #     # if hash_table.get(file_name):
    #     #     found.append(hash_table.get(file_name))

    #     # print(hash_table.get(file_name))

    word_cache = {}
    found = []
    # adds all queries into a cache with empty arr as value
    for word in queries:
        word_cache[word] = []

    # takes care of empty string in cache
    if '' in word_cache:
        del word_cache[''] 

    for path in files:
        split_path = path.split('/')                # split all paths in files by '/'
        file_name = split_path[len(split_path) - 1] # store file name from split_path (files are always last thing in path)
        # print(file_name)
        if file_name in word_cache:                 # check if stored file name is in word_cache
            word_cache[file_name].append(path)      # append the current path we're on to that keys array
    for value in word_cache.values():
        if len(value) > 0:                          # make sure there are values in that key's array
            # print(f'VALUE: {value}')
            found += value                          # add those values to found
    
    return found

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
