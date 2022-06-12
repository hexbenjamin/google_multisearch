# import engines
import scope

import sys
import webbrowser

engine_dict = {
    "google": "https://www.google.com/search?q=^+site%3A^+OR+",
    "google_img": "https://www.google.com/search?tbm=isch&q=^+site%3A^+OR+"
}

def construct_link(query: str, scope_set: int, engine: str):
    search_prefix, site_spec, or_str = engine_dict[engine].split('^')
    
    search_link = search_prefix + query

    for i in range(len(scope_set)):
        if len(scope_set) - 1 != i:
            search_link += site_spec + scope_set[i] + or_str
        else:
            search_link += site_spec + scope_set[i]
    
    return search_link


def main():
    print("welcome to HEX BENJAMIN's replicant_search.")
    
    scope_list = scope.reader('scope.txt')
    engine_list = list(engine_dict.keys())

    ### ENGINE SELECT
    print("please select a search engine to utilize from the following list, by its numerical ID: ")
    
    options = ""
    for i in range(len(engine_list)):
        entry = f'{i}={engine_list[i]}'
        if i != len(engine_list) - 1:
            entry += ' / '
        
        options += entry
    
    while True:
        try:
            engine_id = int(input(f'[{options}]\n'))
            break
        except:
            print('error: not an integer. make sure to select a number, and not a label!')
    
    engine = engine_list[engine_id]

    ### SET SELECT
    print("replicant_search loads links from 'scope.txt'.")
    print("the following scope sets were found. please select one by its numerical ID to proceed.")
    options = ""
    for i in range(len(scope_list)):
        entry = f'{scope_list[i][0]}={scope_list[i][1]}'
        if i != len(engine_list) - 1:
            entry += ' / '
        
        options += entry
    
    while True:
        try:
            selected_set = int(input(f'[{options}]\n'))
            break
        except:
            print('error: not an integer. make sure to select a number, and not a label!')
    
    set_links = scope.set_format(scope_list[selected_set][2])

    ### QUERY SELECT
    print("now, what are we searching for? input your query below, and press [Enter] to search.")
    user_query = input('>> ')

    search_link = construct_link(user_query, set_links, engine)
    print(search_link)

    webbrowser.open(output)
    sys.exit(0)

if __name__ == "__main__":
    main()
