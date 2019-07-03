""" Phrases: classes for various English phrases
Taking a lot of inspiration from
http://faculty.washington.edu/cicero/370syntax.htm

TODO:
 - Abstract out all word forms, make text files with lots of words in them
 - Fix "a"/"an"/etc
 https://www.englishclub.com/vocabulary/regular-verbs-list.htm
 https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx
 https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913
 http://www.ashley-bovan.co.uk/words/partsofspeech.html

"""
import random, words

#all regular and singular, for now
C_CONJ = ["and", "but", "for", "or", "so", "yet"] # Coordinating conjunctions
DETERMINERS = ["the", "this", "that", "my", "your", "his", "her", "its", "our", "their", "one", "each", "every", "another"] #https://www.ef.com/ca/english-resources/english-grammar/determiners/

class Phrase(object):
    """docstring for Phrase."""

    def __init__(self):
        super(Phrase, self).__init__()
        self.words = []

    def __repr__(self):
        return " ".join(self.words)

    def populate(self):
        raise NotImplementedError

class NounPhrase(Phrase):
    """docstring for NounPhrase."""

    def __init__(self):
        super(NounPhrase, self).__init__()
        self.num_adjectives = random.randrange(0,4) #arbitary 4?
        self.num_adverbs = random.randrange(0,2) if self.num_adjectives else 0
        self.noun = str(words.Noun())
        self.populate()

    def generate_adjectives(self):
        self.adjectives = [str(words.Adjective()) for i in range(self.num_adjectives)]
        self.words = self.adjectives + self.words

    def generate_adverbs(self):
        self.adverbs = [str(words.Adverb()) for i in range(self.num_adverbs)]
        self.words = self.adverbs + self.words

    def generate_determiner(self):
        if random.random() < 0.5:
            return None
        else:
            self.determiner = random.choice(DETERMINERS)
            self.words = [self.determiner] + self.words

    def populate(self):
        self.words = [self.noun]
        self.generate_adjectives()
        self.generate_adverbs()
        self.generate_determiner()

class VerbPhrase(Phrase):
    """docstring for VerbPhrase."""

    def __init__(self):
        super(VerbPhrase, self).__init__()
        self.verb = str(words.Verb())
        self.num_adverbs = random.randrange(0,2)
        self.noun_phrase = str(NounPhrase())
        self.populate()

    def generate_adverbs(self):
        self.adverbs = [str(words.Adverb()) for i in range(self.num_adverbs)]
        self.words += self.adverbs

    def populate(self):
        self.words.append(self.verb)
        if random.random() < 0.5:
            self.words.append(self.noun_phrase)
        self.generate_adverbs()

class Sentence(Phrase):
    """docstring for Sentence."""

    def __init__(self):
        super(Sentence, self).__init__()
        self.noun_phrase = NounPhrase()
        self.verb_phrase = VerbPhrase()
        self.populate()

    def populate(self):
        self.words = self.noun_phrase.words + self.verb_phrase.words
        # Coordinating conjunction
        if random.random() < 0.25:
            new_clause = Sentence()
            conjunction = random.choice(C_CONJ)
            self.words.append(conjunction)
            self.words += new_clause.words

    def __repr__(self):
        content = " ".join(self.words) + "."
        return content.capitalize()

if __name__ == '__main__':
    n = Sentence()
    print(n)
