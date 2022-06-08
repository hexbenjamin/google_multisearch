import webbrowser

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


test_link = "https://test.bungled.funk/"
print(link_substitute(test_link))