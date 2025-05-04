from stats import get_num_words, letter_count, list_of_dictionaries
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here
        file_contents = f.read()
        
    return file_contents




def main():
    text = get_book_text(sys.argv[1])
    number_of_words = get_num_words(text)
    number_of_letters = letter_count(text)
    letter_count_variable = letter_count(text)
    list_dict = list_of_dictionaries(letter_count_variable)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for i in list_dict:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")




main()