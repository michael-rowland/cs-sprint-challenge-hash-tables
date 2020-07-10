def has_negatives(a):
    opposites = {}
    correct = []
    for num in a:
        if -num in opposites:
            correct.append(num)
        opposites[num] = -num
    return [i if i>0 else -i for i in correct]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
