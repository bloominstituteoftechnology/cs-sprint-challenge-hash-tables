# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    #setting up dictionary 
    my_dict = {}

    #results list
    result = []

    #making a dict of paths
    for path in files:
        file_item = path.split('/')[-1] # the file is the last name after last / divider

        # if item is in my dictionary 
        if file_item in my_dict:
            my_dict[file_item].append(path) #appending path to locations tht are known
        else:
            my_dict[file_item] = [path] #create a list if item is not in dictionary
    
    #for loop to check queries (if each one is a key in our dictionary)
    for q in queries: 
        if q in my_dict: # if query is in my dictionary 
            results = my_dict[q] # set results to my dictionary 
            # we are returning a list of paths
            for path in results: #we are returning lists into one list
                result.append(path) #appending list of path
    else:
        pass #if not then pass

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
