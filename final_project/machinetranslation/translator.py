""" translator.py """
from deep_translator import MyMemoryTranslator

def english_to_french(englishText):
    """write the code here"""
    translator = MyMemoryTranslator(source='english',target='french')
    french_text = translator.translate(englishText)
    return french_text

def french_to_english(frenchText):
    """write the code here"""
    translator = MyMemoryTranslator(source='french',target='english')
    english_text = translator.translate(frenchText)
    return english_text
