def main():
    with open('/Users/greghering/workspace/github.com/ghering90/bookbot/books/frankenstein.txt', 'r') as file:
        content = file.read()
        #print(content)
    print(count_words(content))
def count_words(text):
    return len(text.split())
    
if __name__ == "__main__":
    main()