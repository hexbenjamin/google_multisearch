import re


engine_dict = {
    "key": ["name", "sequence", "i : imgs_str", "o : or_str", "P: prefix", "Q : q_prefix", "S : site_spec"],
    0: ["google", "PiQSo", "tbm=isch&", "+OR+", "https://www.google.com/search?", "q=", "+site%3A"]
}

# print(engine_dict[0][0]) // print engine name, e.g.

def link_format(link: str):
    out_str = ""
    
    ## determined this to be unnecessary:
    # esc_char = "%25"
    
    for char in link:
        if char == ":":
            char = "%3A"
        elif char == "/":
            char = "%2F"

        out_str += char
    
    return out_str


def reader(fp='scope.txt'):
    scope_list = []
    temp_list = []

    with open(fp, 'r') as scope_file:
        for line in scope_file:
            current = line.strip()
            if not current.startswith("#"):
                if current.startswith("~"):
                    temp_list.clear()
                    set_id, set_label = re.split(":", current)
                    set_id = int(set_id[1:])
                
                if current.startswith("h"):
                    current = link_format(current)
                    temp_list.append(current)

                if current == "end":
                    scope_list.append([(set_id, set_label), temp_list])
                
    
    return scope_list


def select(scope_list=list, id=int):
    selected = scope_list[id]
    selected_label = str(id) + ":" + selected[0][1]
    selected_links = selected[1]
    return selected_label, selected_links


test_reader = reader()
label, links = select(test_reader, 0)
