def main():
    with open('/Users/greghering/workspace/github.com/ghering90/bookbot/books/frankenstein.txt', 'r') as file:
        content = file.read()
        #print(content)
    print("--- Begin report of books/frankenstein.txt ---\n" + str(count_words(content)) + " words found in the document\n")
    for key, value in count_chars(content).items():
        print("The " + key + " character was found " + str(value) + " times")
    print("--- End report ---")
def count_words(text):
    return len(text.split())
def count_chars(text):
    result = {}
    for char in text.lower():
        if char in "abcdefghijklmnopqrstuvwxyz":
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result
    
    
if __name__ == "__main__":
    main()