'''
UNDERSTAND
Example input:
```python
paths = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
]
queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
]
```
Example return value:
```
[ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
```

PLAN:

Create a dict of file names (Keys) and its full path (Value) using Split
then look for each element in queries and append its path to return list 
'''

def finder(files, queries):
    ht = {}
    result = []
    for path in files:
        
        path_file = path.split("/")[-1] 

        if path_file in ht:
            ht[path_file].append(path)
        else:
            ht[path_file] = [path]

    for query in queries:
        if query in ht:
            result = result + ht[query]
        

        
    return result

if __name__ == "__main__":
    files = [
       "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
    ]
    queries = [
       "ls",
    "foo.txt",
    "nosuchfile.txt"
    ]
    print(finder(files, queries))
