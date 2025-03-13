def count_words(text):
    # Split the text into a list of words and return the length
    words = text.split()
    return len(words)

def count_character(text):
    # Create an empty dictionary to store character counts
    char_counts = {}
    
    # Convert text to lowercase so 'A' and 'a' are counted as the same
    lowercase_text = text.lower()
    
    # Count how many times each character appears
    for char in lowercase_text:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
            
    return char_counts

def sort_chars(char_dict):
    # Convert the dictionary into a list of character info
    chars_list = []
    for char in char_dict:
        char_info = {
            "char": char,
            "count": char_dict[char]
        }
        chars_list.append(char_info)
    
    # Sort the list by count (highest to lowest)
    sorted_list = sorted(chars_list, 
                        key=lambda item: item["count"], 
                        reverse=True)
    
    return sorted_list