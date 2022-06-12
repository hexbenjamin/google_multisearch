from posixpath import split
import re


engine_dict = {
    "key": ["sequence", "i : imgs_str", "o : or_str", "P: prefix", "Q : q_prefix", "S : site_spec"],
    0: ["PiQSo", "tbm=isch&", "+OR+", "https://www.google.com/search?", "q=", "+site%3A"]
}

# print(engine_dict[0][0]) // print engine name, e.g.

def set_format(input_set: list):
    formatted_list = []
    for link in input_set:
        out_str = ""
    
        ## determined this to be unnecessary:
        # esc_char = "%25"
        
        for char in link:
            if char == ":":
                char = "%3A"
            elif char == "/":
                char = "%2F"

            out_str += char
        
        formatted_list.append(out_str)
    
    return formatted_list


def reader(fp: str):
    # RETURNS:
    # LIST of (set_id: INT, link: STR) TUPLES

    txt_list = []
    with open(fp, 'r') as scope_file:
        for line in scope_file:
            if not line.isspace() and not line.startswith('#'):
                current = line.strip()
                txt_list.append(current)

    split_list = []
    for entry in txt_list:
        id, link = entry.split('|')
        split_list.append((id, link))

    return split_list


def set_select(split_list: list, set_id: int):
    # RETURNS:
    # LIST of STR links
    
    set_list = []

    for entry in split_list:
        if int(entry[0]) == set_id:
            set_list.append(entry[1])

    return set_list


split_list = reader('scope.txt')

selected = set_select(split_list, 1)
print(selected)

formatted = set_format(selected)
print(formatted)
