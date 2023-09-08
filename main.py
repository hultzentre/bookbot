with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    lower_contents = file_contents.lower()
    print("--- This is a report on the book 'Frankenstein' by Mary Shelly ---")
    print("") 
    print(f"There are {len(words)} words found in the book")
    print("")
    letters = {}
    for i in range(len(lower_contents)):
        current = lower_contents[i]
        if current not in letters:
            letters[current] = 1
        else:
            letters[current] += 1
    
    for letter in letters:
        if letter.isalpha():
            print(f"The character {letter} appears {letters[letter]} times")
    print("")
    print("--- This marks the end of the report ---")


