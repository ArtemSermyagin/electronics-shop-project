from src.keyboard import Keyboard

def test_srt():
    kb = Keyboard("Dark Project KD87A", 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"

# assert str(kb.language) == "EN"
# kb.language = "CH"
# print(kb.language)
# # AttributeError: property 'language' of 'Keyboard' object has no setter