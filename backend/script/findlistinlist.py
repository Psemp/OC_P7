pattern = ["ou", "se", "trouve"]

original_list_1 = ["ou", "se", "trouve", "la", "tour", "eiffel"]

original_list_2 = ["ou", "se", "situe", "la", "tour", "eiffel"]


def subfinder(large_list, sublist):
    matches = []
    for i in range(len(large_list)):
        if large_list[i] == sublist[0] and large_list[i:i+len(sublist)] == sublist:
            matches.append(sublist)

    if len(matches) >= 1:
        return True
    else:
        return False


print(subfinder(original_list_1, pattern))
print(subfinder(original_list_2, pattern))
