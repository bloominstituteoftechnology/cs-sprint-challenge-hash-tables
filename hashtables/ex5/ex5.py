# Your code here
from hashtable import HashTable

hash_table = HashTable()
def finder(files, queries):
    # Your code here
    found = []
    for word in queries:
        # print(f'query: {word}')
        hash_table.put(word, [])
    
    for path in files:
        split_path = path.split('/')
        file_name = split_path[len(split_path) - 1]
        print(path)
        # key = hash_table.hash_index(file_name)
        if hash_table.get(file_name) == []:
            # print('ITS HERE')
            hash_table.get(file_name).append(path)
            found.append(hash_table.get(file_name)[0])
        # if hash_table.get(file_name):
        #     found.append(hash_table.get(file_name))

        # print(hash_table.get(file_name))
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
