def is_unique(str):
    if len(str) > 128: # Assuming ASCII character set
        return False

    is_unique_list = list()
    for char in str:
        if char in is_unique_list:
            return False
        else:
            is_unique_list.append(char)
    return True


string = "dikshaa"
print(is_unique(string))

