from stats import count_words, count_characters, sort_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return(file_contents)

def main():
    path = sys.argv
    if len(path) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(path[1]) 
        sorted_list = sort_dictionary(count_characters(text))
        print('============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------')
        print(f'Found {count_words(text)} total words')
        print('--------- Character Count -------')
        for item in sorted_list:
            if item['char'].isalpha():
                print(f'{item['char']}: {item['num']}')
        print('============= END ===============')

main()