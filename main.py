from stats import count_words, count_character, sort_chars
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(file_path):
    text = get_book_text(file_path)
    word_count = count_words(text)
    char_counts = count_character(text)
    sorted_chars = sort_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_data in sorted_chars:
        char = char_data["char"]
        if char.isalpha():
            print(f"{char}: {char_data['count']}")
    
    print("============= END ===============")

def main():
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Use the file path from command-line argument
    file_path = sys.argv[1]
    print_report(file_path)


if __name__ == '__main__':
    main()