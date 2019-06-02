""" Phrases: classes for various English phrases
Taking a lot of inspiration from
http://faculty.washington.edu/cicero/370syntax.htm

"""
import random

VOWELS = ["a", "e", "i", "o", "u"]

#all regular and singular, for now
DETERMINERS = ["the", "this", "that", "my", "your", "his", "her", "its", "our", "their", "one", "each", "every", "another"] #https://www.ef.com/ca/english-resources/english-grammar/determiners/
ADJECTIVES = ["different", "important", "every", "large", "available", "popular", "able", "basic", "known", "difficult", "hot", "red", "orange", "yellow", "green", "blue", "purple", "traditional", "old", "young", "cold"]
ADVERBS = ["angrily", "accidentally", "anxiously", "coyly", "boldly", "honestly", "justly", "madly", "mysteriously"]
NOUNS = ["people", "history", "way", "art", "world", "information", "map", "family", "government", "system", "computer", "meat", "year", "person"]
VERBS = ["wanted", "used", "worked", "called", "tried", "asked", "needed", "helped", "talked", "moved", "played", "believed", "dreamed", "liked"]

class Phrase(object):
    """docstring for Phrase."""

    def __init__(self):
        super(Phrase, self).__init__()
        self.words = []

    def __repr__(self):
        print(self.words)
        return " ".join(self.words)

    def populate(self):
        raise NotImplementedError

class NounPhrase(Phrase):
    """docstring for NounPhrase."""

    def __init__(self):
        super(NounPhrase, self).__init__()
        self.num_adjectives = random.randrange(0,4) #arbitary 4?
        self.num_adverbs = random.randrange(0,2) if self.num_adjectives else 0
        self.noun = random.choice(NOUNS)
        self.populate()

    def generate_adjectives(self):
        self.adjectives = random.sample(ADJECTIVES, self.num_adjectives)
        self.words = self.adjectives + self.words

    def generate_adverbs(self):
        self.adverbs = random.sample(ADVERBS, self.num_adverbs)
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
        self.verb = random.choice(VERBS)
        self.num_adverbs = random.randrange(0,2)
        self.noun_phrase = str(NounPhrase()) if random.random() < 0.5 else ""
        self.populate()

    def generate_adverbs(self):
        self.adverbs = random.sample(ADVERBS, self.num_adverbs)
        self.words += self.adverbs

    def populate(self):
        self.words = [self.verb, self.noun_phrase]
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

if __name__ == '__main__':
    n = Sentence()
    print(n)
