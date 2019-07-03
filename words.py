import random

VOWELS = ["a", "e", "i", "o", "u"]

with open("dictionary/verbs.txt") as verbfile:
    VERBS = [line.strip() for line in verbfile]

with open("dictionary/nouns.txt") as nounfile:
    NOUNS = [line.strip() for line in nounfile]

with open("dictionary/adverbs.txt") as adverbfile:
    ADVERBS = [line.strip() for line in adverbfile]

with open("dictionary/adjectives.txt") as adjectivefile:
    ADJECTIVES = [line.strip() for line in adjectivefile]

class Word(object):
    """docstring for Words."""

    def __init__(self, dict):
        self.val = random.choice(dict)

    def __repr__(self):
        return str(self.val.strip())

class Noun(Word):
    """Noun docstring"""

    def __init__(self):
        super(Noun, self).__init__(NOUNS)

class Verb(Word):
    """docstring for Verb."""

    def __init__(self):
        super(Verb, self).__init__(VERBS)

    def __repr__(self):
        # comment this out if u want present tense
        penult = self.val[-2]
        ult = self.val[-1]
        if penult in VOWELS and ult not in VOWELS:
            return str(Verb())
        elif penult in VOWELS and ult == "y":
            return self.val + "ed"
        elif penult not in VOWELS and ult == "y":
            return self.val[:-1] + "ied"
        elif ult == "e":
            return self.val + "d"
        else:
            return self.val + "ed"

class Adverb(Word):
    """docstring for Adverb."""

    def __init__(self):
        super(Adverb, self).__init__(ADVERBS)

class Adjective(Word):
    """docstring for Adjective."""

    def __init__(self):
        super(Adjective, self).__init__(ADJECTIVES)
