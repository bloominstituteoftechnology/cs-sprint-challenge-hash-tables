# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    hashtable = dict()

    # We can use the built in string method to separate filenames from paths
    for name in files:
        filename = name.rsplit('/',1)[-1]

        # By using filename as the key, we can have a list of names as the value,
        # similar to Markov exercise
        if filename not in hashtable:
            hashtable[filename] = []
            hashtable[filename].append(name)
        
        else:
            hashtable[filename].append(name)
    
    # Instantiate result:
    result = []

    # Check queries agains filenames
    for q in queries:
       if q in hashtable:
           for filepath in hashtable[q]:
               result.append(filepath)

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
