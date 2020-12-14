from string import whitespace, punctuation

"""
* TextSplitter *

This is TextSplitter class, which splits the contents of the given text file into
text and grammer and whitespace.

"""


class TextSplitter:
    def __init__(self, filename):
        self.fn = filename

        with open("source/" + filename, 'r') as fp:
            self.contents = fp.read()

        self.name = filename[:-4]
        self.path = "results/" + self.name + "/"

    def partition_words(self):
        words = []
        words_lowercase = []

        for word in self.contents.split():
            if word.isalpha():
                words.append(word.strip())
                words_lowercase.append(word.strip().lower())

        with open(self.path+'words.txt', 'w') as fp:
            fp.write("\n".join(words))
            print("Written words onto a file.")

        with open(self.path+'words_lower.txt', 'w') as fp:
            fp.write("\n".join(words_lowercase))
            print("Written lowercase words onto a file.")

    def partition(self):
        alpha_raw = ""
        alpha_with_whitespace = ""
        binary_raw = ""
        punctuations = ""
        punctuation_with_whitespace = ""
        whitespaces = ""

        for c in self.contents:
            if c in whitespace:
                whitespaces += c
                punctuation_with_whitespace += c
                alpha_with_whitespace += c

            if c in punctuation:
                punctuations += c
                punctuation_with_whitespace += c

            if c.isalpha():
                alpha_raw += c
                alpha_with_whitespace += c
                binary_raw += str(ord(c)) + " "

        with open(self.path+'alpha_raw.txt', 'w') as fp:
            print('Written raw alphabets onto a file.')
            fp.write(alpha_raw)

        with open(self.path+'alpha_with_whitespace.txt', 'w') as fp:
            print('Written alphabets with whitespaces onto a file.')
            fp.write(alpha_with_whitespace)

        with open(self.path+'binary_raw.txt', 'w') as fp:
            print('Written binary raw onto a file.')
            fp.write(binary_raw)

        with open(self.path+'punctuations.txt', 'w') as fp:
            print('Written raw punctuations onto a file.')
            fp.write(punctuations)

        with open(self.path+'punctuation_with_whitespace.txt', 'w') as fp:
            print('Written punctuations with whitespaces onto a file.')
            fp.write(punctuation_with_whitespace)

        with open(self.path+'whitespaces.txt', 'w') as fp:
            print('Written raw whitespaces onto a file.')
            fp.write(whitespaces)
