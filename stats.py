
def get_num_words(text):
    split_text = text.split()
    return len(split_text)

def letter_count(text):
    letter_count_dict = {}
    for character in text.lower():
         if character in letter_count_dict:
            letter_count_dict[character] += 1
         else:
             letter_count_dict[character] = 1
    return letter_count_dict

def sort_on(dict):
    return dict["num"]

def list_of_dictionaries(dictionary):
    new_dict ={}
    dict_list = []
    for i in dictionary:
        new_dict = {"char": i, "num": dictionary[i]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

