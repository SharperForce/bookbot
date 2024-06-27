def main():
    path = "books/frankenstein.txt"
    file_content = open_book(path)
    word_count = count_words(file_content)
    char_counted = char_count(file_content)
    cleaned = clean_char(char_counted)
    sorted_dict = sort_dict(cleaned)
    format_report(word_count,sorted_dict,path)

def open_book(path):
    with open (path) as f:
        content = f.read()
    return content

def count_words(x):
    words = x.split()
    return (len(words))

def char_count(x):
    char_dict = {}
    x = x.lower()
    for items in x:
        if items in char_dict:
            char_dict[items] = char_dict[items] + 1
        else:
            char_dict[items] = 1
    return char_dict

def clean_char(dict):
    x = []
    for item in dict:
        if not item.isalpha():
            x.append(item)
    for items in x:    
        del(dict[items])
    return dict


def sort_on(x):
    return x['count']

def sort_dict(char_dict):
    char_list = []
    for items in char_dict:
        char_list.append({"letter":items, "count":char_dict[items]})
    char_list.sort(reverse=True,key=sort_on)
    return char_list


def format_report(word_count,char_dict,path):
    print(f'---Report for {path} ---')
    print(f'{path} contains {word_count} words')
    print()
    for items in char_dict:
        count = items['count']
        letter = items['letter']
        print(f'The letter \'{letter}\' appears {count} times in the text')
    print('End of report')


main()