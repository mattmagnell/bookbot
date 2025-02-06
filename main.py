

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = get_word_count(text)
    print(f"--- Report of {book_path} --- ")
    print(f"{word_count} words found in document")
    character_count = count_characters(text)
    sorted_dict = dict_to_list(character_count)
    for dict in sorted_dict:
        print(f"the '{dict["char"]}' was found {dict["num"]} times")
    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def dict_to_list(dict):
    new_list = [{"char": key, "num": value} for key, value in dict.items() if key.isalpha()]
    new_list.sort(key=sort_on, reverse=True)
    return new_list

def sort_on(dict):
    return dict["num"] 
  
  
main()



