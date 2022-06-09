import os
import sys
import webbrowser


engine_dict = {
    "key": ["search_prefix", "site_specifier", "or_operand"],
    "google": ["https://www.google.com/search?", "site%3A", "+OR+"]
}

def scope_reader(fp: str):
    scope_list = []
    with open(fp, 'r') as list_file:
        in_list = list_file.readlines()
        for site in in_list:
            scope_list.append(site.strip())
    return scope_list


def link_substitute(link: str):
    out_str = ""
    
    ## determined this to be unnecessary:
    ## once the search happens, the link is formatted to use a % (%25) escape
    ## if the escape characters are included in the input link, the colons & slashes are escaped in the actual search
    ## (maybe let's just let google do as google does today)
    
    # esc_char = "%25"
    
    for char in link:
        if char == ":":
            char = "%3A"
        elif char == "/":
            char = "%2F"

        out_str += char
    
    return out_str

def scope_format(fp: str):
    in_list = scope_reader(fp)
    scope_list = []
    for site in in_list:
            formatted = link_substitute(site)
            scope_list.append(formatted)
    return scope_list

def construct_link(query: str, scope_file='scope.txt', engine='google', mode='std'):
    prefix, add_site, or_str = engine_dict[engine]
    
    if mode == 'img':
        prefix += "tbm=isch&"

    scope = scope_format(scope_file)

    validated_query = ""
    for letter in query:
        if letter == " ":
            letter = "+"
        validated_query += letter
    validated_query = "q=" + validated_query
    
    out_link = prefix + validated_query + "+"
    
    for i in range(len(scope)):
        current_link = scope[i]
        if len(scope) - i == 1:
            out_link += add_site + current_link
        else:
            out_link += add_site + current_link + or_str
    
    return out_link

def main():
    print("welcome to HEX BENJAMIN's multi_search.")

    # print("what search engine would you like to use for the operation?")
    # engine = input('>>')

    engine = "google"

    print("multi_search will load scope links from 'scope.txt' by default.")
    print("press [Enter] to continue, or specify the path to a different .txt file.")
    custom_scope = input('>> ')

    print("now, what are we searching for? input your query below.")
    user_query = input('>> ')

    if custom_scope != "":
        output = construct_link(user_query, custom_scope)
    else:
        output = construct_link(user_query)

    input(f"press [Enter] to start a search for '{user_query}'.")

    webbrowser.open(output)
    sys.exit(0)

if __name__ == "__main__":
    main()