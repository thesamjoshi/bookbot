def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_book_words(file_contents)
        char_count = count_book_characters(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("\n")
    
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"The {char} character was found {char_count[char]} times")
    print("--- End report ---")


def count_book_words(book_content):
    words = book_content.split()
    return len(words)

def count_book_characters(book_content):
    count = {}
    
    for char in book_content:
        if char.isalpha():
            count[char.lower()] = 0
    
    for char in book_content:
        if char.isalpha():
            count[char.lower()] += 1
    
    return count

main()