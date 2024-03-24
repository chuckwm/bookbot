def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num_words = count_words(text)
    counted_letters = count_letters(text)
    best = sorted([(v,k) for (k,v) in counted_letters.items()], reverse=True)
    report = create_report(book, num_words, best)
    print(report)

def get_book_text(book):
    with open(book) as f:
        return f.read()

def count_words(text):
    count = text.split()
    return len(count)

def count_letters(text):
    letters = dict()
    for letter in text.lower():
        if letter.isalpha():
            letters[letter] = letters.get(letter,0)+1
    return letters


def create_report(book, num_words, best):
    body = ""
    body += f"--- Begin report of {book} ---\n"
    body += f"{num_words} words found in the document\n\n"
    for count, letter in best:
        body += f"The '{letter}' character was found {count} times\n"
    body += "--- End report ---"
    report = f"""
{body}
    """
    return report
#    letters.add(

if __name__ == '__main__':
    main()




