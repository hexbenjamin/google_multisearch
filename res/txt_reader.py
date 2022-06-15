def make_list(fp: str):
    txt_list = []
    with open(fp, 'r') as txt_file:
        for line in txt_file:
            if not line.isspace() and not line.startswith('#'):
                current = line.strip()
                txt_list.append(current)
    return txt_list