import sys
from stats import get_num_words, pretty_character_count
from stats import get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(filepath):
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    character_count = get_character_count(book_text)
    character_count_pretty = pretty_character_count(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in character_count_pretty:
        char = pair["char"]
        num = pair["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])

if __name__ == '__main__':
    main()