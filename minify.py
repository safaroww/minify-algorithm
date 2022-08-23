def minify(html):
    result = ''
    before_is_white = False
    in_quote = False
    for char in html:
        if char == '\n':
            continue

        if char in '\"\'':
            if not in_quote:
                in_quote = char
            else:
                if in_quote == char:
                    in_quote = False

        if char in ' \t':
            if in_quote:
                before_is_white = False
            elif before_is_white:
                continue
            else:
                before_is_white = True
                result += char
                continue

        before_is_white = False 
        result += char
    return result



def create_new_file(file_name, content):
    splitted_name = file_name.split('.')
    new_name = splitted_name[0] + '.min.' + splitted_name[1]
    with open(new_name, 'w') as file:
        file.write(content)


if __name__ == '__main__':
    file_name = input('Minify etmek istediyiniz faylin adini girin: ')
    with open(file_name, 'r') as file:
        content = file.read()
    minified_content = minify(content)
    create_new_file(file_name, minified_content)
    print(f'{file_name} uğurla minify edildi!')