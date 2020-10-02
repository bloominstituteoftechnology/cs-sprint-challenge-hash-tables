def finder(files, queries):
    # Your code here

    # create a dict of paths
    pth_dict = {}

    # for filename(s) in path of every file
    for i in files:
        filename = i.split('/')[-1] # split filename(s) at the forward slash and then move back in the index one 
        if filename not in pth_dict: # check if filename not in dict
            pth_dict[filename] = []
        pth_dict[filename].append(i) # add it

    output = []

    # iterateve over qs, if it's in the dict, add it to output
    # append doesn't work as it adds all as one vs. need to use extend which adds every applicable one by one
    for i in queries:
        if i in pth_dict:
            output.extend(pth_dict[i])
    
    return output

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
