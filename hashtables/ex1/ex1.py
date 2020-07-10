def get_indices_of_item_weights(weights, length, limit):
    storage = {}
    for idx, weight in enumerate(weights):
        target = limit - weight
        if target in storage:
            return idx, storage[target]
        storage[weight] = idx
    return None
