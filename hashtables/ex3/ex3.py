def intersection(arrays):
    counter = {}
    for idx, array in enumerate(arrays):
        for i in array:
            if i not in counter:
                counter[i] = []
            counter[i].append(idx)
    # there is probably a faster way to do this?
    return [k for k, v in counter.items() if len(v) == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
