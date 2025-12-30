def num_words(text):
    return len(text.split())

def character_count(text):
    counts = {}

    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

def dict_sorted(char_dict):
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)

