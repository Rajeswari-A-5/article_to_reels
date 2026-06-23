from deep_translator import GoogleTranslator


def translate_text(text, language="ta"):

    translated = GoogleTranslator(

        source="auto",

        target=language

    ).translate(text)

    return translated