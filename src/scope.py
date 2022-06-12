import re


def reader(fp: str):
    # RETURNS:
    # LIST of [id: int, label: str, links: list] LISTS

    out_list = []

    txt_list = []
    with open(fp, 'r') as scope_file:
        for line in scope_file:
            if not line.isspace() and not line.startswith('#'):
                current = line.strip()
                txt_list.append(current)

    temp_list = []
    labels = []
    for entry in txt_list:
        if '|' in entry:
            id, link = entry.split('|')
        
            if link.startswith('#'):
                label = link.strip('#')
                labels.append((id, label))
            else:
                temp_list.append((id, link))

    for e in labels:
        id = e[0]
        label = e[1]
        set_links = [x[1] for x in temp_list if x[0] == id]

        out_list.append([id, label, set_links])

    return out_list


def set_format(input_set: list):
    # RETURNS:
    # LIST of *FORMATTED* STR links
    
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


# print(reader('scope.txt'))

# selected = set_select(split_list, 1)
# print(selected)

# formatted = set_format(selected)
# print(formatted)
