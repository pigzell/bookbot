def count_words(text):
    words = text.split()
    return(len(words))

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_on(item):
    return item['num']

def sort_dictionary(dict):
    list = []
    for key, value in dict.items():
        temp_dict = {}
        temp_dict['char'] = key
        temp_dict['num'] = value
        list.append(temp_dict)
    list.sort(reverse=True, key=sort_on)
    return list