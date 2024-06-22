# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def count_word(p_book_text):
    dic_letters = {}
    words_book = p_book_text.split()
    for word in words_book:
        letters_eval = [*word]

        for letterEval in letters_eval:
            letterEvalUpper=letterEval.upper()
            if letterEvalUpper in dic_letters:
                dic_letters[letterEvalUpper] += 1
            else:
                dic_letters[letterEvalUpper] = 1
    return dic_letters


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    file = "books/frankenstein.txt"
    with open(file) as f:
        dic_letters = {}
        dic_letters_sort = {}
        file_contents = f.read()
        words = file_contents.split()
        dic_letters = count_word(file_contents)

        print(f"--- Begin report of {file} ---")
        print(f"{len(words)} words found in the document")
        dic_letters_sort = sorted(dic_letters.items(), key=lambda x:x[1], reverse=True)
        for lettersSort in dic_letters_sort:
            if lettersSort[0].isalpha():
                print(f"The '{lettersSort[0]}' character was found {lettersSort[1]} times")

        print(f"--- End report ---")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
