def finder(files, queries):
    """
    Find files that match the provided filename, and return their full file paths.
    """
    # Create hash table for storing filenames:
    file_locations = {}
    # Populate our hash table with filenames for lookup (key) and all locations/filepaths (list of values) 
    # of files with that name:
    for filepath in files:
        # Get the filename only (we will use this as the lookup key in the hash table):
        filename = filepath.split("/")[-1]
        # If filename already in hash table, then append this location (filepath) to the associated list:
        if filename in file_locations:
            file_locations[filename].append(filepath)
        # If no files with this name in hash table yet, then add it:
        else:
            file_locations[filename] = [filepath]

    # Lookup each filename in queries, and if it exists in our file storage system, 
    # then return all locations (filepaths) of files with that filename:
    result = []
    for filename in queries:
        if filename in file_locations:
            for filepath in file_locations[filename]:
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
