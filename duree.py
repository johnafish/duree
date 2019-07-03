""" Duree: an experiment in linguistics.

This module procedurally generates a body of text following basic English
phrase structure rules. It writes the text to an HTML file which can be
uploaded to Amazon KDP and printed.

TODO:
    * Increase randomness in optional phrase structures
    * Allow for recursive phrase structures
    * Wider dictionary
    * Better selection of articles given nouns

NOTES:
    * A limit of 335000 seems to be around the maximum limit that KDP will take
"""
import random, phrases

class Book(object):
    """docstring for Book."""

    def __init__(self, l):
        super(Book, self).__init__()
        self.volume_length = l
        self.volume_num = 1
        self.num_volumes = 15
        self.total_length = 0

    def generate(self):
        """generate book"""
        for i in range(self.num_volumes):
            self.gen_volume()
        print("Printing complete.")
        print("Total length of {0} words.".format(self.total_length))

    def gen_volume(self):
        """generate volume"""
        output_file = open("output/vol{0}.html".format(self.volume_num), "w")
        book = ""
        real_length = 0
        book += "<html><body style='font-size: 7pt'>"
        while real_length < self.volume_length:
            chapter = self.gen_chapter()
            book += "<p>{0}</p>\n".format(chapter)
            real_length += len(chapter.split(" "))
        book += "</body></html>"
        output_file.write(book)
        output_file.close()
        self.total_length += real_length
        print("Printed volume {0}".format(self.volume_num))
        self.volume_num += 1


    def gen_chapter(self):
        """generate chapter"""
        num_paragraphs = random.randrange(30, 50)
        paragraphs = [self.gen_paragraph() for i in range(num_paragraphs)]
        return "\n".join(paragraphs)

    def gen_paragraph(self):
        """generate paragraph"""
        num_sentences = random.randrange(5, 8)
        sentences = [str(phrases.Sentence()) for i in range(num_sentences)]
        return "<p>{0}</p>".format(" ".join(sentences))

if __name__ == '__main__':
    random.seed(1234567890)
    DUREE = Book(800000)
    DUREE.generate()
