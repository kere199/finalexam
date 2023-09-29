def count_func(input_str):
    char_count = {}
    result_count = 0

    for char in input_str:
        if char.isalnum():
            char_lower = char.lower()
            char_count[char_lower] = char_count.get(char_lower, 0) + 1
            if char_count[char_lower] == 2:
                result_count += 1

    return result_count

input_string = "aA111"
print(count_func(input_string))

