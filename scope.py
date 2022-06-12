### REPLICANT_SEARCH - SCOPE PROCESSING FUNCTIONS

def make_list(txt_list: list):
    # RETURNS:
    # LIST of [id: int, label: str, links: list] LISTS

    out_list = []
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


def format_set(input_set: list):
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

