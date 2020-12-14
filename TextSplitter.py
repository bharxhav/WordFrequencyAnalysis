from string import whitespace, punctuation

"""
* TextSplitter *

This is TextSplitter class, which splits the contents of the given text file into
text and grammer and whitespace.

"""


class TextSplitter:
    def __init__(self, filename):
        # Saving the FileName
        self.fn = filename

        with open(filename, 'r') as fp:
            # Saving the File Contents
            self.contents = fp.read()

    def partition(self):
        r = ""
        p = ""
        w = ""

        for c in self.contents:
            if c in whitespace:
                w += c
            elif c in punctuation:
                p += c
            else:
                r += c

        fp = open(self.fn[:-4] + "/text_raw.txt", 'w')
        fp.write(r)
        fp.close()
        fp = open(self.fn[:-4] + "/text_whitespaces.txt", 'w')
        fp.write(w)
        fp.close()
        fp = open(self.fn[:-4] + "/text_punctuation.txt", 'w')
        fp.write(p)
        fp.close()

        # Keep dumping to readable file..
