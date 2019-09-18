#INF200 ex01 Task C
#Counting letters

#Defining counting letters function
def letter_freq(txt):
    letters_counts = {}
    for character in txt.lower():
        if character in letters_counts.keys():
            letters_counts[character] += 1
        else:
            letters_counts[character] = 1
    return letters_counts


if __name__ == "__main__":
    text = input("Please enter text to analyse: ")

    frequencies = letter_freq(text)
    for letter, count in sorted(frequencies.items()):  #printing sorted frequencies of letters
        print('{:3}{:10}'.format(letter, count))