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


def validated_input(check: list):
    while True:
        user_in = exit_check(input('>> '))
        
        try:
            user_in = int(user_in)
            if user_in in range(len(check)):
                break
            else:
                print(make_error() + ' not in range. make sure to select a number included in the list!')
        except:
            print(make_error() + 'not an integer. make sure to select a number, and not a label!')
    
    return user_in


# color shortcuts
def color_progress(label: str):
    return txt_color(label, fg='mn', bg='wn')


def color_options(options: str):
    return txt_color(options, fg='yn')


def make_error():
    return txt_color("ERROR!", fg='wb', bg='rb') + " "


def make_note():
    return txt_color("NOTE:", fg='wb', bg='cb') + " "


# begin!
def main():
    colorama_init()
    
    prog_name = txt_color('REPLICANT_SEARCH', bg='gb')
    dev_name = txt_color('HEX BENJAMIN', 'bb')
    
    print('welcome to ' + prog_name + '.')
    print('developed with love (& little experience) by ' + dev_name + '.')
    
    txt = txt_reader.make_list('scopes.txt')
    scope_list = scope.make_list(txt)
    engine_list = list(engine_dict.keys())

    ### ENGINE SELECT
    print('---\n' + color_progress('[1/3]') + ' : engine_select')

    print("please select a search engine to utilize from the following list, by its numerical ID: ")
    
    options = ""
    for i in range(len(engine_list)):
        entry = f'{i}={engine_list[i]}'
        if i != len(engine_list) - 1:
            entry += ' / '
        
        options += entry
    
    
    print(color_options(f'[{options}]'))

    engine_id = validated_input(engine_list)
    
    engine = engine_list[engine_id]

    ### SET SELECT
    print('---\n' + color_progress('[2/3]') + ' : set_select')

    # print("replicant_search loads links from 'scope.txt'.")
    print("the following scope sets were found. please select one by its numerical ID to proceed.")
    # print(make_note() + " add a ? after any set ID to list the links it contains.")

    options = ""
    for i in range(len(scope_list)):
        entry = f'{scope_list[i][0]}={scope_list[i][1]}'
        if i != len(engine_list) - 1:
            entry += ' / '
        
        options += entry
    
    print(color_options(f'[{options}]'))

    selected_set = validated_input(scope_list)
    selected_set = scope_list[selected_set][2]
    
    set_links = scope.set_format(selected_set)
    
    ### QUERY SELECT
    print('---\n' + color_progress('[3/3]') + ' : query_input')

    print("now, what are we searching for? input your query below, and press " + color_options('[Enter]') + " to search.")
    user_query = exit_check(input('>> '))

    search_link = construct_link(user_query, set_links, engine)

    webbrowser.open(search_link)
    
    ### END/RESTART
    print('---\n')

    restart = input("begin another search? [Y=restart, !Y=exit]\n")
    if restart.upper() == 'Y':
        main()
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
