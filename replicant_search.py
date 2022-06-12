# import project modules
from colorizer import txt_color, colorama_init
import scope
import txt_reader

# import system modules
import sys
import webbrowser

engine_dict = {
    "google": "https://www.google.com/search?q=^+site%3A^+OR+",
    "google_img": "https://www.google.com/search?tbm=isch&q=^+site%3A^+OR+"
}

def exit_check(input: str):
    if input.lower() == "exit":
        sys.exit(2)
    else:
        return input


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
    colorama_init()

    print('welcome to ' + txt_color('REPLICANT_SEARCH', bg='gb') + '.')
    print(txt_color('developed with love (& little experience) by ', 'wd') + txt_color('HEX BENJAMIN', 'bn') + '.')
    
    txt = txt_reader.make_list('scopes.txt')
    scope_list = scope.make_list(txt)
    engine_list = list(engine_dict.keys())

    print('---\n[1/] engine_select')

    ### ENGINE SELECT
    print("please select a search engine to utilize from the following list, by its numerical ID: ")
    
    options = ""
    for i in range(len(engine_list)):
        entry = f'{i}={engine_list[i]}'
        if i != len(engine_list) - 1:
            entry += ' / '
        
        options += entry
    
    while True:
        engine_id = exit_check(input(f'[{options}]\n>> '))
        
        try:
            engine_id = int(engine_id)
            if engine_id in range(len(engine_list)):
                break
            else:
                print('error: not in range. make sure to select a number included in the list!')
        except:
            print('error: not an integer. make sure to select a number, and not a label!')
    
    engine = engine_list[engine_id]

    print('---\n[2/] set_select')

    ### SET SELECT
    print("replicant_search loads links from 'scope.txt'.")
    print("the following scope sets were found. please select one by its numerical ID to proceed.\n[*] add a ? after any set ID to list the links it contains.")
    options = ""
    for i in range(len(scope_list)):
        entry = f'{scope_list[i][0]}={scope_list[i][1]}'
        if i != len(engine_list) - 1:
            entry += ' / '
        
        options += entry
    
    while True:
        selected_set = exit_check(input(f'[{options}]\n>> '))
        try:
            selected_set = int(selected_set)
            if selected_set in range(len(scope_list)):
                break
            else:
                print('error: not in range. make sure to select a number included in the list!')
        except:
            print('error: not an integer. make sure to select a number, and not a label!')
    
    set_links = scope.set_format(scope_list[selected_set][2])

    ### QUERY SELECT
    print("now, what are we searching for? input your query below, and press [Enter] to search.")
    user_query = exit_check(input('>> '))

    search_link = construct_link(user_query, set_links, engine)

    webbrowser.open(search_link)
    
    restart = input("begin another search? [Y=restart, !Y=exit]\n")
    if restart.upper() == 'Y':
        main()
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
