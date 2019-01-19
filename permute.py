

def perm_gen_lex(string):
    """recursively returns array of all possible character permutations of given string in lexicographical order"""

    ascii_counter = 0

    # base case
    if len(string) == 0:
        return []
    if len(string) < 2:
        return [string]

    perm_list = []

    # loop through each char in string
    for i in range(len(string)):

        # remove and store char
        c = string[i]
        next_string = remove_at(i, string)

        # recurse
        temp_list = perm_gen_lex(next_string)

        # construct final list
        for temp_string in temp_list:
            perm_list.append(c + temp_string)

    return perm_list


def remove_at(i, string):
    """returns string without char at index i"""

    return string[:i] + string[i+1:]

