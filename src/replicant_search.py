# import engines
import scope

import sys
import webbrowser

engine_dict = {
    "google": "https://www.google.com/search?q=^+site%3A^+OR+",
    "google_img": "https://www.google.com/search?tbm=isch&q=^+site%3A^+OR+"
}

def construct_link(query: str, scope_set: int, engine="google"):
    search_prefix, site_spec, or_str = engine_dict[engine].split('^')
    
    # '{search_prefix} + query + {site_spec} + scope0 + {or_str} + {site_spec} + scope1'



def main():
    print("welcome to HEX BENJAMIN's multi_search.")
    
    scope_list = scope.reader('scope.txt')
    engine_list = list(engine_dict.keys())

    ### ENGINE SELECT
    print("please select a search engine to utilize from the following list: ")
    
    options = ""
    for i in range(len(engine_list)):
        entry = f'{i}={engine_list[i]}'
        if i != len(engine_list) - 1:
            entry += ' / '
        
        options += entry
    
    engine = input(f'[{options}]')

    

    ### QUERY SELECT
    print("now, what are we searching for? input your query below.")
    user_query = input('>> ')



    # webbrowser.open(output)
    # sys.exit(0)

# if __name__ == "__main__":
#     main()

# print(construct_link('https://thangs.com/', 'google_img'))

main()