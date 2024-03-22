'''
 CS 230 Program 3 - Wikipedia Processing
 Sun Ma (CS230)
 Add a description

'''

from string import punctuation



#this function prints section header
def section_header(title, width=40):
    length_on_side = (width - len(title)) // 2
    print("=" * width)
    print()
    print(title.center(width - (length_on_side // 4)))
    print()
    print("=" * width)

#counts the word and digits
def word_and_digit_count(text):
    search_string = "Bentley"
    characters = 0
    total_words = 0
    years_count = 0
    count_digits = 0
    sentences = text.split(".")
    total_sentences = len(sentences)
    words = text.split()
    total_words += len(words)

    for _ in text:
        characters += 1

    for word in words:
        if word.isdigit() and len(word) == 4:
            years_count += 1

    for char in text:
        if char.isdigit():
            count_digits += 1

    count = text.count(search_string)

    average_words_in_sentence = float(characters) / float(total_sentences)

    print(("Sentences: " + str(total_sentences)).center(40))
    print(("Words: " + str(total_words)).center(40))
    print(("Characters: " + str(characters)).center(40))
    print(f"Average sentence length: {average_words_in_sentence:.2f}".center(40))
    print(("Digits: " + str(count_digits)).center(40))
    print(("Years: " + str(years_count)).center(40))
    print(f"The Search string {search_string} appears {count} times in the file.".center(40))

#this function processes the words
def process_words(text,specified_word):
    import string
    words = text.split()
    #adds ** to the start and the end of the key word
    for i in range(len(words)):
        vowel_count = 0
        if words[i] == specified_word:
            words[i] = "**" + words[i] + "**"
        else:
            #changes any punctuation to #
            for char in words[i]:
                if char in string.punctuation:
                    words[i] = words[i].replace(char, "#")
            #adds _ between the word that has a length between 2 to 4
            if len(words[i]) == 1:
                words[i] = words[i].upper()
            elif 2 <= len(words[i]) <= 4:
                word_index = ''
                for char in words[i]:
                    word_index += char + '_'
                words[i] = word_index[:-1]
            #swaps the case of the vowels if there are more than two vowels in a word
            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            for char in words[i]:
                if char in vowels:
                    vowel_count += 1

            if vowel_count >= 2:
                processing = ''
                for char in words[i]:
                    if char in vowels:
                        processing += char.swapcase()
                    else:
                        processing += char

                    words[i] = processing
            #omits the [] and anything in between it
            new_text = ''
            in_brackets = False
            for char in words[i]:
                if char == '[':
                    in_brackets = True
                    continue
                elif char == ']':
                    in_brackets = False
                    continue
                if not in_brackets:
                    new_text += char

                words[i] = new_text
    #join the wrods back into a single text called updated_text
    updated_text = " ".join(words)

    return updated_text

#print the words
def print_words(text, max_line_length=45, justification='left'):
    lines = []
    currentline = ""
    linenumber = 1
    #limit the amount of words
    for word in text.split():
        if len(currentline + word) + 1 <= max_line_length:
            if currentline:
                currentline += " " + word
            else:
                currentline += word
        else:
            if justification == 'r':
                lines.append(f"{linenumber} {currentline.rjust(max_line_length)}")
            elif justification == 'c':
                lines.append(f"{linenumber} {currentline.center(max_line_length)}")
            else:
                lines.append(f"{linenumber} {currentline}")
            currentline = word
            linenumber += 1

    if currentline:
        if justification == 'r':
            lines.append(f"{linenumber} {currentline.rjust(max_line_length)}")
        elif justification == 'c':
            lines.append(f"{linenumber} {currentline.center(max_line_length)}")
        else:
            lines.append(f"{linenumber} {currentline}")

    for line in lines:
        print(line)

#runs all of these
def main():
    import parameters
    text = parameters.text
    spec = parameters.spec
    section_header("File Analysis", 40)
    word_and_digit_count(text)
    section_header("Original Text", 60)
    print_words(text, spec[1], 'l')
    section_header("Updated Text",40)
    print_words(process_words(text,"Bentley"), spec[1],spec[2])


main()


