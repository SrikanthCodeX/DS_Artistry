# delete duplicates in sorted Array
# time complexity is O(N)

def remove_duplicates(array):

    if not array:
        return []

    unique_items = [array[0]]

    for item in array:
        if item != unique_items[-1]:
            unique_items.append(item)
    return unique_items


array = [2,2,5,5,4,3,6,4,9]
without_duplicates = remove_duplicates(sorted(array))

print(without_duplicates)
