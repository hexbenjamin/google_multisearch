from bs4 import BeautifulSoup

import requests

def list_from_table(table):
    out_list = [["index", "char", "Win-1252", "UTF-8"]]
    i = 0
    with open('utf_log.txt', 'w') as log_file:
        for row in table:
            log_file.write(f'entry #{i}:\n')
            row_list = [str(i)]
            current_row = table[i]
            log_str = ""
            
            if row_list[0] == "x":
                print("")

            for entry in current_row.stripped_strings:
                # row_list.append(repr(entry))
                log_str += repr(entry) + " | "


            if row_list[0] == "0":
                i += 1
            else:
                out_list.append(row_list)
                i += 1
            
            log_file.write(log_str + "\n")
            
        
    return out_list


def fix_ws(target: str):
    print(target)


r = requests.get('https://www.w3schools.com/tags/ref_urlencode.asp')
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.find('table', class_='ws-table-all')

rows = table.find_all('tr')
rows_list = list_from_table(rows)