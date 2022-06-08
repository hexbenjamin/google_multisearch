import webbrowser


engine_dict = {
    "key": ["search_prefix", "site_specifier", "or_operand"],
    "google": ["https://www.google.com/search?q=", "+site%253A", "+OR"]
}


def link_substitute(link):
    out_str = ""
    esc_char = "%25"
    for char in link:
        if char == ":":
            char = esc_char + "3A"
        elif char == "/":
            char = esc_char + "2F"

        out_str += char
    
    return out_str

def site_list_format(engine: str, fp: str):
    sites_list = []
    prefix, add_site, or_str = engine_dict[engine]
    with open(fp, 'r') as list_file:
        in_list = list_file.readlines()
        for site in in_list:
            formatted = link_substitute(site.strip())
            sites_list.append(formatted)
    return sites_list


print(site_list_format("google", "sites.txt"))