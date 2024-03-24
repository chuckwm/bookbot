def main():
    with open("books/frankenstein.txt") as f: 
    # ... 
        file_contents = f.read()
        words = file_contents.split()
        print(len(words))

if __name__ == '__main__':
    main()



