import random
from modules.first.word_finder import Word
sentence=""
word_instance = Word()
adjectives=[]
adverbs=[]
conjunctions=[]
determiner=[]
duplicators=[]
interjections=[]
nouns=[]
numerals=[]
postpositive=[]
pronouns=[]
questions=[]
verbs=[]

with open('ClassifiedVerbs//Adjective.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            adjectives.append(word)
with open('ClassifiedVerbs/Adverb.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            adverbs.append(word)
with open('ClassifiedVerbs/Conjunction.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            conjunctions.append(word)
with open('ClassifiedVerbs/Determiner.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            determiner.append(word)
with open('ClassifiedVerbs/Duplicator.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            duplicators.append(word)
with open('ClassifiedVerbs/Interjection.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            interjections.append(word)
with open('ClassifiedVerbs/Noun.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            nouns.append(word)
with open('ClassifiedVerbs/Numeral.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            numerals.append(word)
with open('ClassifiedVerbs/PostPositive.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            postpositive.append(word)
with open('ClassifiedVerbs/Pronoun.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            pronouns.append(word)
with open('ClassifiedVerbs/Question.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            questions.append(word)
with open('ClassifiedVerbs/Verb.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        for word in line.split():
            verbs.append(word)






def getSentence(value):
    adjc = random.randrange(0, len(adjectives))
    advrb = random.randrange(0, len(adverbs))
    cnjctn = random.randrange(0, len(conjunctions))
    dtrmnr = random.randrange(0, len(determiner))
    dplctr = random.randrange(0, len(duplicators))
    intrjctn = random.randrange(0, len(interjections))
    noun = random.randrange(0, len(nouns))
    nmrl = random.randrange(0, len(numerals))
    ppstv = random.randrange(0, len(postpositive))
    prnon = random.randrange(0, len(pronouns))
    qustn = random.randrange(0, len(questions))
    verb = random.randrange(0, len(verbs))
    while True:
        if (value < 200):
            sentence = nouns[noun] + " " + verbs[verb]
        elif (value > 200 and value < 350):
            sentence = nouns[noun] + " " + conjunctions[cnjctn] + " " + verbs[verb]
        elif (value >= 350 and value < 450):
            sentence = adjectives[adjc] + " " + nouns[noun] + " " + conjunctions[cnjctn] + " " + verbs[verb]
        elif (value >= 450 and value < 600):
            sentence = adjectives[adjc] + " " + nouns[noun] + " " + conjunctions[cnjctn] + " " + adverbs[advrb] + " " + \
                       verbs[verb]
        elif (value >= 600 and value < 750 ):
            sentence = adjectives[adjc] + " " + nouns[noun] + " " + conjunctions[cnjctn] + " " + adverbs[advrb] + " " + \
                   verbs[verb] + " " + conjunctions[cnjctn % 8 + 1] + " " + pronouns[prnon] + " " + verbs[
                       verb % 5 + 1]
        else:
            sentence = adjectives[adjc] + " " + nouns[noun] + " " + conjunctions[cnjctn] + " " + adverbs[advrb] + " " + \
                       verbs[verb] + " " + conjunctions[cnjctn % 8 + 1] + " " + pronouns[prnon] + " "+interjections[intrjctn] +" "+ verbs[
                           verb % 5 + 1]
        sentence = sentence+"."

        if(word_instance.get_word_value(word=sentence)==value):
            return (sentence)
        else:
            adjc = random.randrange(0, len(adjectives))
            advrb = random.randrange(0, len(adverbs))
            cnjctn = random.randrange(0, len(conjunctions))
            dtrmnr = random.randrange(0, len(determiner))
            dplctr = random.randrange(0, len(duplicators))
            intrjctn = random.randrange(0, len(interjections))
            noun = random.randrange(0, len(nouns))
            nmrl = random.randrange(0, len(numerals))
            ppstv = random.randrange(0, len(postpositive))
            prnon = random.randrange(0, len(pronouns))
            qustn = random.randrange(0, len(questions))
            verb = random.randrange(0, len(verbs))
