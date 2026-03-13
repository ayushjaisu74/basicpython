from googletrans import Translator

def translate_word_cli(word):
    translator = Translator()
    translated = translator.translate(word, src='en', dest='hi')
    return translated.text

# Example usage:
word_to_translate = input("Enter an English word to translate to Hindi: ")
translated_text = translate_word_cli(word_to_translate)
print(f"Translated to Hindi: {translated_text}")