import json

file = 'translation.json'

class Translator:
    def __init__(self, word_to_translate):
        self.word_to_translate = word_to_translate

    def en_to_fr(self):
        with open(file) as f:
            data = json.load(f)

        for word in data:
            if word == self.word_to_translate:
                return json.dumps(data[word])

    def fr_to_en(self):
        with open(file) as f:
            data = json.load(f)

        for word, translation in data.items():
            if self.word_to_translate == translation:
                return json.dumps(word)

def translate():
    lang = input("Which language do you wish to translate to? English or French? (Type 'en' for English, or 'fr' for French) >")
    ask = input("What's the word you wish to translate? >")
    translator = Translator(ask)

    if (lang.lower() == "fr"):
        return translator.en_to_fr()
    
    elif (lang.lower() == "en"):
        return translator.fr_to_en()

print(translate())