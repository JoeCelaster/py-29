def replace_with_rank(arr):
    sorted_unique = sorted(set(arr))
    rank_map = {value: index + 1 for index, value in enumerate(sorted_unique)}

    return [rank_map[x] for x in arr]


# Example
arr = [100, 2, 70, 2]
print(replace_with_rank(arr))
