import spacy
nlp = spacy.load('en')
doc = nlp(u'I am learning how to build chatbots')
for token in doc:
    print(token.text, token.pos)