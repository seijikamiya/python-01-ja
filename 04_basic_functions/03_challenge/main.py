def unique_substrings(input_string):
    # 「pass」を削除して、ここにコードを書いてください
    unique_substrings_list = []
    for i in range(len(input_string)):
        for j in range(i+1, len(input_string)+1):
            substring = input_string[i:j]
            if substring not in unique_substrings_list:
                unique_substrings_list.append(substring)
    return unique_substrings_list


input_string = "banana"
print(unique_substrings(input_string))
