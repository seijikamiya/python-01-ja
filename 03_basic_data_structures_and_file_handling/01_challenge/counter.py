def counter():
    occurrences = {}
    fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "kiwi",
        "banana",
        "melon",
        "orange",
        "strawberry",
    ]

    # ここにコードを書いてください
    for fruit in fruits:
        if fruit in occurrences:
            occurrences[fruit] += 1
        else:
            occurrences[fruit] = 1

    for key, value in occurrences.items():
        print(f'{key}: {value}')        

    return occurrences

print(counter())
