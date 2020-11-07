# Your code here

class File_Node:
    def __init__(self, filename):
        self.filename = filename
        self.next = None


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    path_dict = {}
    for file in files:
        query_name = file.split('/')[-1]
        if query_name not in path_dict:
            path_dict[query_name] = File_Node(file)
        else:
            current = path_dict[query_name]
            while current.next:
                current = current.next
            current.next = File_Node(file)

    result = []
    for query in queries:
        if query in path_dict:
            current = path_dict[query]
            while current:
                result.append(current.filename)
                current = current.next

    return result


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
