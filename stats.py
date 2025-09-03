def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_counts(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def sort_char_counts(char_counts):
    sorted_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]

    def sort_key(entry):
        return entry["num"]

    sorted_list.sort(key=sort_key, reverse=True)
    return sorted_list
