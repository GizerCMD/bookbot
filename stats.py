def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    character = {}
    for char in text.lower():
        character[char] = character.get(char, 0) + 1

    return character

def sort_helper(item):
    return item["num"]

def pretty_character_count(character_count):
    result = []
    for char, count in character_count.items():
        temp = {"char": char, "num": count}
        result.append(temp)

    result.sort(key=sort_helper, reverse=True)
    return result