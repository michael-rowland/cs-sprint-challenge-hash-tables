def finder(files, queries):
    storage = {}
    for path in files:
        file_name = path.split("/")[-1]
        if file_name not in storage:
            storage[file_name] = []
        storage[file_name].append(path)

    result = []
    for query in queries:
        if query in storage:
            result += storage[query]
    return result


if __name__ == "__main__":
    files = ["/bin/foo", "/bin/bar", "/usr/bin/baz"]
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
