import random

class Book(object):
    """docstring for Book."""

    def __init__(self, articles, nouns, prepositions, adjectives, verbs, output_file):
        super(Book, self).__init__()
        self.articles = articles
        self.nouns = nouns
        self.prepositions = prepositions
        self.adjectives = adjectives
        self.verbs = verbs
        self.output_file = open(output_file, "w")

    def generate(self):
        """generate book"""
        num_chapters = random.randrange(10,20)
        book = ""
        for i in range(num_chapters):
            book += "<h1>Chapter {0}</h1>".format(i+1)
            book += "<p>{0}</p>".format(self.gen_chapter())
        self.output_file.write(book)
        self.output_file.close()
        return

    def gen_chapter(self):
        """generate chapter"""
        num_paragraphs = random.randrange(30,50)
        paragraphs = [self.gen_paragraph() for i in range(num_paragraphs)]
        return "\n".join(paragraphs)

    def gen_paragraph(self):
        """generate paragraph"""
        num_sentences = random.randrange(5,8)
        sentences = [self.gen_sentence() for i in range(num_sentences)]
        return "<p>{0}</p>".format(" ".join(sentences))

    def gen_sentence(self):
        """generate sentence"""
        noun_phrase = self.gen_noun_phrase()
        verb_phrase = self.gen_verb_phrase()
        return "{0} {1}.".format(noun_phrase, verb_phrase).capitalize()

    def gen_noun_phrase(self):
        """generate noun phrase"""
        article = random.choice(self.articles)
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        return "{0} {1} {2}".format(article, adjective, noun)

    def gen_prep_phrase(self):
        """generate prepositional phrase"""
        preposition = random.choice(self.prepositions)
        noun_phrase = self.gen_noun_phrase()
        return "{0} {1}".format(preposition, noun_phrase)

    def gen_verb_phrase(self):
        """generate noun phrase"""
        verb = random.choice(self.verbs)
        noun_phrase = self.gen_noun_phrase()
        prep_phrase = self.gen_prep_phrase()
        return "{0} {1} {2}".format(verb, noun_phrase, prep_phrase)


if __name__ == '__main__':
    random.seed(1234567890)
    articles = ["a", "the"]
    nouns = ["cat", "dog", "squid", "man", "cow", "boy", "girl"]
    prepositions = ["in", "on", "from", "near"]
    adjectives = ["red", "green", "fast", "slow", "talented"]
    verbs = ["ate", "drank", "watched", "read", "wrote", "eats", "dreamed"]
    duree = Book(articles, nouns, prepositions, adjectives, verbs, "output.html")
    print(duree.generate())
