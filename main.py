from stats import num_words, character_count, dict_sorted

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)


    word_count = num_words(text)
    char_counts = character_count(text)
    sorted_chars = dict_sorted(char_counts)

    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()