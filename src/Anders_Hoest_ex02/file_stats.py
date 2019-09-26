__author__ = 'Anders Mølmen Høst'
__email__ = 'anderhos@nmbu.no'

def char_counts(textfilename):

"""open file in UTF-8 counting characters into a string"""
    output = [0] * 256

    with open(textfilename, 'r', encoding='UTF--8') as file:
        for character in file.read():
            output[ord(character)] +=1
        return output

if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )